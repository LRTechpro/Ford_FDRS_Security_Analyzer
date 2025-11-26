"""
Database Manager for Log Parser History
Stores parsed logs, errors, and statistics for trend analysis
"""

import sqlite3
import json
from datetime import datetime
from typing import List, Dict, Any, Optional
from pathlib import Path


class DatabaseManager:
    """Manages SQLite database for log history and statistics"""
    
    def __init__(self):
        self.db_dir = Path.home() / '.log_parser'
        self.db_file = self.db_dir / 'log_history.db'
        self._ensure_db_dir()
        self._init_database()
    
    def _ensure_db_dir(self):
        """Create database directory if it doesn't exist"""
        self.db_dir.mkdir(parents=True, exist_ok=True)
    
    def _get_connection(self):
        """Get database connection"""
        return sqlite3.connect(self.db_file)
    
    def _init_database(self):
        """Initialize database schema"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        # Logs table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                filepath TEXT NOT NULL,
                parse_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                file_type TEXT,
                file_size INTEGER,
                vehicle_vin TEXT,
                total_items INTEGER,
                total_errors INTEGER,
                total_successes INTEGER,
                total_warnings INTEGER,
                root_cause_type TEXT,
                root_cause_summary TEXT
            )
        ''')
        
        # Errors table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS errors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                log_id INTEGER,
                line_number INTEGER,
                timestamp TEXT,
                severity TEXT,
                ecu_address TEXT,
                ecu_name TEXT,
                nrc_code TEXT,
                description TEXT,
                is_critical BOOLEAN,
                FOREIGN KEY (log_id) REFERENCES logs(id)
            )
        ''')
        
        # ECU statistics table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ecu_stats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                log_id INTEGER,
                ecu_address TEXT,
                ecu_name TEXT,
                error_count INTEGER,
                success_count INTEGER,
                last_seen TIMESTAMP,
                FOREIGN KEY (log_id) REFERENCES logs(id)
            )
        ''')
        
        # NRC code frequency table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS nrc_frequency (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                log_id INTEGER,
                nrc_code TEXT,
                count INTEGER,
                description TEXT,
                FOREIGN KEY (log_id) REFERENCES logs(id)
            )
        ''')
        
        # Create indexes for faster queries
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_logs_date ON logs(parse_date)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_errors_log ON errors(log_id)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_errors_ecu ON errors(ecu_address)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_errors_nrc ON errors(nrc_code)')
        
        conn.commit()
        conn.close()
    
    def store_log_session(self, filename: str, filepath: str, file_type: str, 
                          results: List[Dict], summary: Dict, root_cause: Dict = None) -> int:
        """Store a complete log parsing session"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        try:
            # Get file size
            file_size = Path(filepath).stat().st_size if Path(filepath).exists() else 0
            
            # Extract VIN if present
            vin = self._extract_vin(results)
            
            # Insert log record
            cursor.execute('''
                INSERT INTO logs (
                    filename, filepath, file_type, file_size, vehicle_vin,
                    total_items, total_errors, total_successes, total_warnings,
                    root_cause_type, root_cause_summary
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                filename, filepath, file_type, file_size, vin,
                summary.get('total', 0),
                summary.get('errors', 0),
                summary.get('successes', 0),
                summary.get('warnings', 0),
                root_cause.get('most_likely_issue', '') if root_cause else '',
                root_cause.get('proximate_cause', '') if root_cause else ''
            ))
            
            log_id = cursor.lastrowid
            
            # Store individual errors
            self._store_errors(cursor, log_id, results)
            
            # Store ECU statistics
            self._store_ecu_stats(cursor, log_id, results)
            
            # Store NRC code frequency
            self._store_nrc_frequency(cursor, log_id, results)
            
            conn.commit()
            return log_id
            
        except Exception as e:
            conn.rollback()
            print(f"Error storing log session: {e}")
            return -1
        finally:
            conn.close()
    
    def _extract_vin(self, results: List[Dict]) -> Optional[str]:
        """Extract VIN from results if present"""
        for result in results:
            result_str = str(result).upper()
            # Look for VIN patterns
            if 'VIN' in result_str or 'F190' in result_str:
                # Try to extract 17-character VIN
                import re
                vin_match = re.search(r'\b[A-HJ-NPR-Z0-9]{17}\b', result_str)
                if vin_match:
                    return vin_match.group()
        return None
    
    def _store_errors(self, cursor, log_id: int, results: List[Dict]):
        """Store error entries"""
        for result in results:
            # Check if it's an error
            result_str = str(result).lower()
            is_error = any(keyword in result_str for keyword in ['error', 'fail', 'critical'])
            
            if is_error:
                severity = result.get('severity', 'ERROR').upper()
                line_num = result.get('line_number', 0)
                timestamp = result.get('log_timestamp', '')
                
                # Extract ECU info
                ecu_address = ''
                ecu_name = ''
                nrc_code = ''
                
                if result.get('nrc_explanations'):
                    nrc_code = result['nrc_explanations'][0].get('code', '')
                
                description = result.get('line', result.get('text', ''))[:500]  # Limit length
                
                is_critical = severity in ['CRITICAL', 'FATAL']
                
                cursor.execute('''
                    INSERT INTO errors (
                        log_id, line_number, timestamp, severity,
                        ecu_address, ecu_name, nrc_code, description, is_critical
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    log_id, line_num, timestamp, severity,
                    ecu_address, ecu_name, nrc_code, description, is_critical
                ))
    
    def _store_ecu_stats(self, cursor, log_id: int, results: List[Dict]):
        """Store ECU statistics"""
        # Count errors and successes per ECU
        ecu_stats = {}
        
        # This would be enhanced with actual ECU detection from results
        # For now, storing basic stats
        
        pass  # Placeholder for ECU statistics
    
    def _store_nrc_frequency(self, cursor, log_id: int, results: List[Dict]):
        """Store NRC code frequency"""
        nrc_counts = {}
        
        for result in results:
            if result.get('nrc_explanations'):
                for nrc in result['nrc_explanations']:
                    code = nrc.get('code', '')
                    if code:
                        if code not in nrc_counts:
                            nrc_counts[code] = {
                                'count': 0,
                                'description': nrc.get('explanation', '')
                            }
                        nrc_counts[code]['count'] += 1
        
        for code, data in nrc_counts.items():
            cursor.execute('''
                INSERT INTO nrc_frequency (log_id, nrc_code, count, description)
                VALUES (?, ?, ?, ?)
            ''', (log_id, code, data['count'], data['description']))
    
    def get_recent_logs(self, limit: int = 20) -> List[Dict]:
        """Get recent log sessions"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, filename, filepath, parse_date, file_type,
                   total_items, total_errors, total_successes,
                   root_cause_type
            FROM logs
            ORDER BY parse_date DESC
            LIMIT ?
        ''', (limit,))
        
        columns = [desc[0] for desc in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        conn.close()
        return results
    
    def get_log_details(self, log_id: int) -> Optional[Dict]:
        """Get detailed information about a specific log"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM logs WHERE id = ?', (log_id,))
        row = cursor.fetchone()
        
        if not row:
            conn.close()
            return None
        
        columns = [desc[0] for desc in cursor.description]
        log_data = dict(zip(columns, row))
        
        # Get errors for this log
        cursor.execute('''
            SELECT * FROM errors WHERE log_id = ?
            ORDER BY line_number
        ''', (log_id,))
        
        error_columns = [desc[0] for desc in cursor.description]
        log_data['errors'] = [dict(zip(error_columns, row)) for row in cursor.fetchall()]
        
        conn.close()
        return log_data
    
    def get_error_trends(self, days: int = 30) -> Dict[str, List]:
        """Get error trends over time"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT DATE(parse_date) as date,
                   SUM(total_errors) as errors,
                   SUM(total_warnings) as warnings,
                   COUNT(*) as sessions
            FROM logs
            WHERE parse_date >= datetime('now', '-' || ? || ' days')
            GROUP BY DATE(parse_date)
            ORDER BY date
        ''', (days,))
        
        dates = []
        errors = []
        warnings = []
        sessions = []
        
        for row in cursor.fetchall():
            dates.append(row[0])
            errors.append(row[1])
            warnings.append(row[2])
            sessions.append(row[3])
        
        conn.close()
        
        return {
            'dates': dates,
            'errors': errors,
            'warnings': warnings,
            'sessions': sessions
        }
    
    def get_most_common_nrc_codes(self, limit: int = 10) -> List[Dict]:
        """Get most frequently occurring NRC codes"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT nrc_code, SUM(count) as total_count, description
            FROM nrc_frequency
            GROUP BY nrc_code
            ORDER BY total_count DESC
            LIMIT ?
        ''', (limit,))
        
        results = []
        for row in cursor.fetchall():
            results.append({
                'code': row[0],
                'count': row[1],
                'description': row[2]
            })
        
        conn.close()
        return results
    
    def search_logs(self, query: str, search_type: str = 'filename') -> List[Dict]:
        """Search logs by various criteria"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        if search_type == 'filename':
            sql = '''
                SELECT id, filename, filepath, parse_date, total_errors
                FROM logs
                WHERE filename LIKE ?
                ORDER BY parse_date DESC
            '''
            cursor.execute(sql, (f'%{query}%',))
        elif search_type == 'vin':
            sql = '''
                SELECT id, filename, filepath, parse_date, vehicle_vin, total_errors
                FROM logs
                WHERE vehicle_vin LIKE ?
                ORDER BY parse_date DESC
            '''
            cursor.execute(sql, (f'%{query}%',))
        
        columns = [desc[0] for desc in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        conn.close()
        return results
    
    def delete_old_logs(self, days: int = 90) -> int:
        """Delete logs older than specified days"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            DELETE FROM logs
            WHERE parse_date < datetime('now', '-' || ? || ' days')
        ''', (days,))
        
        deleted_count = cursor.rowcount
        conn.commit()
        conn.close()
        
        return deleted_count
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get overall database statistics"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        stats = {}
        
        # Total logs
        cursor.execute('SELECT COUNT(*) FROM logs')
        stats['total_logs'] = cursor.fetchone()[0]
        
        # Total errors
        cursor.execute('SELECT SUM(total_errors) FROM logs')
        stats['total_errors'] = cursor.fetchone()[0] or 0
        
        # Most problematic files
        cursor.execute('''
            SELECT filename, COUNT(*) as parse_count, AVG(total_errors) as avg_errors
            FROM logs
            GROUP BY filename
            ORDER BY avg_errors DESC
            LIMIT 5
        ''')
        stats['problematic_files'] = [
            {'filename': row[0], 'parse_count': row[1], 'avg_errors': row[2]}
            for row in cursor.fetchall()
        ]
        
        conn.close()
        return stats
