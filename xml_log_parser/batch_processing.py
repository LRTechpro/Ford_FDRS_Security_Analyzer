"""
Professional Batch Processing System
Enterprise-grade batch analysis and automation capabilities
"""

import os
import json
import threading
import logging
from datetime import datetime
from typing import List, Dict, Any, Optional, Callable
from pathlib import Path
import time
import queue
from dataclasses import dataclass, asdict
from concurrent.futures import ThreadPoolExecutor, as_completed
import sqlite3


@dataclass
class BatchJob:
    """Batch processing job definition"""
    job_id: str
    name: str
    description: str
    input_files: List[str]
    output_directory: str
    analysis_profile: str
    created_at: datetime
    status: str = "pending"  # pending, running, completed, failed
    progress: float = 0.0
    estimated_duration: Optional[int] = None
    actual_duration: Optional[int] = None
    error_message: Optional[str] = None
    results_summary: Optional[Dict[str, Any]] = None


@dataclass
class BatchResult:
    """Batch processing result"""
    job_id: str
    file_path: str
    status: str
    analysis_time: float
    error_count: int
    warning_count: int
    success_count: int
    output_file: Optional[str] = None
    error_message: Optional[str] = None


class BatchProcessingEngine:
    """Professional batch processing and automation engine"""
    
    def __init__(self, max_workers: int = 4):
        self.logger = logging.getLogger(__name__)
        self.max_workers = max_workers
        self.job_queue = queue.Queue()
        self.active_jobs: Dict[str, BatchJob] = {}
        self.completed_jobs: Dict[str, BatchJob] = {}
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        
        # Database for job persistence
        self.db_path = "batch_jobs.db"
        self._initialize_database()
        
        # Job callbacks
        self.job_started_callbacks: List[Callable] = []
        self.job_progress_callbacks: List[Callable] = []
        self.job_completed_callbacks: List[Callable] = []
        
        # Load persisted jobs
        self._load_persisted_jobs()
        
        # Start background worker
        self.worker_thread = threading.Thread(target=self._worker_loop, daemon=True)
        self.worker_thread.start()
        
        self.logger.info(f"Batch processing engine initialized with {max_workers} workers")
    
    def _initialize_database(self):
        """Initialize SQLite database for job persistence"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS batch_jobs (
                        job_id TEXT PRIMARY KEY,
                        name TEXT NOT NULL,
                        description TEXT,
                        input_files TEXT,
                        output_directory TEXT,
                        analysis_profile TEXT,
                        created_at TEXT,
                        status TEXT,
                        progress REAL,
                        estimated_duration INTEGER,
                        actual_duration INTEGER,
                        error_message TEXT,
                        results_summary TEXT
                    )
                ''')
                
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS batch_results (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        job_id TEXT,
                        file_path TEXT,
                        status TEXT,
                        analysis_time REAL,
                        error_count INTEGER,
                        warning_count INTEGER,
                        success_count INTEGER,
                        output_file TEXT,
                        error_message TEXT,
                        created_at TEXT,
                        FOREIGN KEY (job_id) REFERENCES batch_jobs (job_id)
                    )
                ''')
                
                conn.commit()
                
        except Exception as e:
            self.logger.error(f"Database initialization failed: {e}")
    
    def _load_persisted_jobs(self):
        """Load persisted jobs from database"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute('''
                    SELECT * FROM batch_jobs 
                    WHERE status IN ('pending', 'running')
                ''')
                
                for row in cursor.fetchall():
                    job_data = dict(zip([col[0] for col in cursor.description], row))
                    job_data['input_files'] = json.loads(job_data['input_files'])
                    job_data['created_at'] = datetime.fromisoformat(job_data['created_at'])
                    
                    if job_data['results_summary']:
                        job_data['results_summary'] = json.loads(job_data['results_summary'])
                    
                    job = BatchJob(**job_data)
                    
                    if job.status == 'running':
                        job.status = 'pending'  # Reset running jobs to pending
                    
                    self.active_jobs[job.job_id] = job
                    self.job_queue.put(job.job_id)
                    
        except Exception as e:
            self.logger.error(f"Failed to load persisted jobs: {e}")
    
    def create_batch_job(self, 
                        name: str,
                        description: str,
                        input_files: List[str],
                        output_directory: str,
                        analysis_profile: str = "comprehensive") -> str:
        """Create a new batch processing job"""
        
        # Generate unique job ID
        job_id = f"batch_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{len(self.active_jobs):03d}"
        
        # Validate input files
        valid_files = []
        for file_path in input_files:
            if os.path.exists(file_path) and os.path.isfile(file_path):
                valid_files.append(file_path)
            else:
                self.logger.warning(f"Input file not found: {file_path}")
        
        if not valid_files:
            raise ValueError("No valid input files provided")
        
        # Ensure output directory exists
        os.makedirs(output_directory, exist_ok=True)
        
        # Create job
        job = BatchJob(
            job_id=job_id,
            name=name,
            description=description,
            input_files=valid_files,
            output_directory=output_directory,
            analysis_profile=analysis_profile,
            created_at=datetime.now(),
            estimated_duration=self._estimate_duration(valid_files)
        )
        
        # Persist job
        self._persist_job(job)
        
        # Add to queue
        self.active_jobs[job_id] = job
        self.job_queue.put(job_id)
        
        self.logger.info(f"Created batch job '{name}' with {len(valid_files)} files")
        return job_id
    
    def _estimate_duration(self, input_files: List[str]) -> int:
        """Estimate job duration based on file sizes and historical data"""
        total_size = sum(os.path.getsize(f) for f in input_files if os.path.exists(f))
        
        # Simple estimation: ~1 second per MB + overhead
        estimated_seconds = max(30, (total_size / (1024 * 1024)) * 1.5 + len(input_files) * 5)
        
        return int(estimated_seconds)
    
    def _persist_job(self, job: BatchJob):
        """Persist job to database"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute('''
                    INSERT OR REPLACE INTO batch_jobs 
                    (job_id, name, description, input_files, output_directory, 
                     analysis_profile, created_at, status, progress, 
                     estimated_duration, actual_duration, error_message, results_summary)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    job.job_id,
                    job.name,
                    job.description,
                    json.dumps(job.input_files),
                    job.output_directory,
                    job.analysis_profile,
                    job.created_at.isoformat(),
                    job.status,
                    job.progress,
                    job.estimated_duration,
                    job.actual_duration,
                    job.error_message,
                    json.dumps(job.results_summary) if job.results_summary else None
                ))
                conn.commit()
                
        except Exception as e:
            self.logger.error(f"Failed to persist job {job.job_id}: {e}")
    
    def _worker_loop(self):
        """Background worker loop for processing jobs"""
        while True:
            try:
                # Get next job (blocks until available)
                job_id = self.job_queue.get(timeout=1)
                
                if job_id in self.active_jobs:
                    job = self.active_jobs[job_id]
                    self._process_job(job)
                
            except queue.Empty:
                continue
            except Exception as e:
                self.logger.error(f"Worker loop error: {e}")
    
    def _process_job(self, job: BatchJob):
        """Process a batch job"""
        try:
            self.logger.info(f"Starting batch job: {job.name}")
            
            # Update job status
            job.status = "running"
            job.progress = 0.0
            start_time = time.time()
            self._persist_job(job)
            self._notify_job_started(job)
            
            # Process files
            results = []
            total_files = len(job.input_files)
            
            for i, file_path in enumerate(job.input_files):
                try:
                    self.logger.info(f"Processing file {i+1}/{total_files}: {os.path.basename(file_path)}")
                    
                    # Process single file
                    result = self._process_single_file(job, file_path)
                    results.append(result)
                    
                    # Update progress
                    job.progress = ((i + 1) / total_files) * 100
                    self._persist_job(job)
                    self._notify_job_progress(job)
                    
                except Exception as e:
                    self.logger.error(f"Error processing {file_path}: {e}")
                    error_result = BatchResult(
                        job_id=job.job_id,
                        file_path=file_path,
                        status="failed",
                        analysis_time=0,
                        error_count=0,
                        warning_count=0,
                        success_count=0,
                        error_message=str(e)
                    )
                    results.append(error_result)
                    self._persist_result(error_result)
            
            # Job completed
            job.status = "completed"
            job.progress = 100.0
            job.actual_duration = int(time.time() - start_time)
            job.results_summary = self._create_job_summary(results)
            
            self._persist_job(job)
            self._notify_job_completed(job)
            
            # Move to completed jobs
            self.completed_jobs[job.job_id] = job
            del self.active_jobs[job.job_id]
            
            self.logger.info(f"Batch job completed: {job.name} ({job.actual_duration}s)")
            
        except Exception as e:
            # Job failed
            job.status = "failed"
            job.error_message = str(e)
            job.actual_duration = int(time.time() - start_time) if 'start_time' in locals() else 0
            
            self._persist_job(job)
            self.logger.error(f"Batch job failed: {job.name} - {e}")
            
            # Move to completed jobs
            self.completed_jobs[job.job_id] = job
            del self.active_jobs[job.job_id]
    
    def _process_single_file(self, job: BatchJob, file_path: str) -> BatchResult:
        """Process a single file within a batch job"""
        start_time = time.time()
        
        try:
            # Here you would integrate with your existing analysis engines
            # For now, this is a placeholder that simulates processing
            
            # Simulate processing time
            time.sleep(0.5)  # Remove in production
            
            # Create output filename
            input_name = Path(file_path).stem
            output_file = os.path.join(job.output_directory, f"{input_name}_analysis_report.html")
            
            # Simulate analysis results
            error_count = 5  # Would come from actual analysis
            warning_count = 12
            success_count = 100
            
            result = BatchResult(
                job_id=job.job_id,
                file_path=file_path,
                status="completed",
                analysis_time=time.time() - start_time,
                error_count=error_count,
                warning_count=warning_count,
                success_count=success_count,
                output_file=output_file
            )
            
            # Persist result
            self._persist_result(result)
            
            return result
            
        except Exception as e:
            result = BatchResult(
                job_id=job.job_id,
                file_path=file_path,
                status="failed",
                analysis_time=time.time() - start_time,
                error_count=0,
                warning_count=0,
                success_count=0,
                error_message=str(e)
            )
            
            self._persist_result(result)
            return result
    
    def _persist_result(self, result: BatchResult):
        """Persist batch result to database"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute('''
                    INSERT INTO batch_results 
                    (job_id, file_path, status, analysis_time, error_count, 
                     warning_count, success_count, output_file, error_message, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    result.job_id,
                    result.file_path,
                    result.status,
                    result.analysis_time,
                    result.error_count,
                    result.warning_count,
                    result.success_count,
                    result.output_file,
                    result.error_message,
                    datetime.now().isoformat()
                ))
                conn.commit()
                
        except Exception as e:
            self.logger.error(f"Failed to persist result: {e}")
    
    def _create_job_summary(self, results: List[BatchResult]) -> Dict[str, Any]:
        """Create summary of job results"""
        total_files = len(results)
        successful = len([r for r in results if r.status == "completed"])
        failed = total_files - successful
        
        total_errors = sum(r.error_count for r in results)
        total_warnings = sum(r.warning_count for r in results)
        total_successes = sum(r.success_count for r in results)
        
        total_analysis_time = sum(r.analysis_time for r in results)
        
        return {
            "total_files": total_files,
            "successful_analyses": successful,
            "failed_analyses": failed,
            "success_rate": (successful / total_files * 100) if total_files > 0 else 0,
            "total_errors": total_errors,
            "total_warnings": total_warnings,
            "total_successes": total_successes,
            "total_analysis_time": total_analysis_time,
            "average_time_per_file": total_analysis_time / total_files if total_files > 0 else 0
        }
    
    # Callback management
    def add_job_started_callback(self, callback: Callable[[BatchJob], None]):
        """Add callback for job started events"""
        self.job_started_callbacks.append(callback)
    
    def add_job_progress_callback(self, callback: Callable[[BatchJob], None]):
        """Add callback for job progress events"""
        self.job_progress_callbacks.append(callback)
    
    def add_job_completed_callback(self, callback: Callable[[BatchJob], None]):
        """Add callback for job completed events"""
        self.job_completed_callbacks.append(callback)
    
    def _notify_job_started(self, job: BatchJob):
        """Notify job started callbacks"""
        for callback in self.job_started_callbacks:
            try:
                callback(job)
            except Exception as e:
                self.logger.error(f"Job started callback error: {e}")
    
    def _notify_job_progress(self, job: BatchJob):
        """Notify job progress callbacks"""
        for callback in self.job_progress_callbacks:
            try:
                callback(job)
            except Exception as e:
                self.logger.error(f"Job progress callback error: {e}")
    
    def _notify_job_completed(self, job: BatchJob):
        """Notify job completed callbacks"""
        for callback in self.job_completed_callbacks:
            try:
                callback(job)
            except Exception as e:
                self.logger.error(f"Job completed callback error: {e}")
    
    # Public API methods
    def get_job_status(self, job_id: str) -> Optional[BatchJob]:
        """Get status of a batch job"""
        if job_id in self.active_jobs:
            return self.active_jobs[job_id]
        elif job_id in self.completed_jobs:
            return self.completed_jobs[job_id]
        else:
            return None
    
    def get_active_jobs(self) -> List[BatchJob]:
        """Get list of active jobs"""
        return list(self.active_jobs.values())
    
    def get_completed_jobs(self, limit: int = 50) -> List[BatchJob]:
        """Get list of completed jobs"""
        jobs = list(self.completed_jobs.values())
        jobs.sort(key=lambda x: x.created_at, reverse=True)
        return jobs[:limit]
    
    def get_job_results(self, job_id: str) -> List[BatchResult]:
        """Get results for a specific job"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute('''
                    SELECT * FROM batch_results WHERE job_id = ?
                    ORDER BY created_at
                ''', (job_id,))
                
                results = []
                for row in cursor.fetchall():
                    result_data = dict(zip([col[0] for col in cursor.description], row))
                    # Remove database-specific fields
                    result_data.pop('id', None)
                    result_data.pop('created_at', None)
                    
                    results.append(BatchResult(**result_data))
                
                return results
                
        except Exception as e:
            self.logger.error(f"Failed to get job results: {e}")
            return []
    
    def cancel_job(self, job_id: str) -> bool:
        """Cancel a pending or running job"""
        if job_id in self.active_jobs:
            job = self.active_jobs[job_id]
            
            if job.status == "pending":
                job.status = "cancelled"
                self._persist_job(job)
                
                # Move to completed
                self.completed_jobs[job_id] = job
                del self.active_jobs[job_id]
                
                self.logger.info(f"Cancelled job: {job.name}")
                return True
            elif job.status == "running":
                # Mark for cancellation (actual cancellation would need more complex implementation)
                job.status = "cancelling"
                self._persist_job(job)
                return True
        
        return False
    
    def delete_job(self, job_id: str) -> bool:
        """Delete a job and its results"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute('DELETE FROM batch_results WHERE job_id = ?', (job_id,))
                conn.execute('DELETE FROM batch_jobs WHERE job_id = ?', (job_id,))
                conn.commit()
            
            # Remove from memory
            self.active_jobs.pop(job_id, None)
            self.completed_jobs.pop(job_id, None)
            
            self.logger.info(f"Deleted job: {job_id}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to delete job {job_id}: {e}")
            return False
    
    def export_job_summary(self, job_id: str, output_path: str) -> bool:
        """Export job summary to JSON file"""
        try:
            job = self.get_job_status(job_id)
            if not job:
                return False
            
            results = self.get_job_results(job_id)
            
            export_data = {
                "job": asdict(job),
                "results": [asdict(r) for r in results],
                "exported_at": datetime.now().isoformat()
            }
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=2, default=str)
            
            self.logger.info(f"Job summary exported: {output_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Export failed: {e}")
            return False
    
    def shutdown(self):
        """Shutdown batch processing engine"""
        self.logger.info("Shutting down batch processing engine")
        self.executor.shutdown(wait=True)


class ScheduledTaskManager:
    """Manage scheduled batch processing tasks"""
    
    def __init__(self, batch_engine: BatchProcessingEngine):
        self.batch_engine = batch_engine
        self.logger = logging.getLogger(__name__)
        self.scheduled_tasks = {}
        
        # Task scheduler thread
        self.scheduler_running = True
        self.scheduler_thread = threading.Thread(target=self._scheduler_loop, daemon=True)
        self.scheduler_thread.start()
    
    def schedule_recurring_job(self, 
                             name: str,
                             input_directory: str,
                             output_directory: str,
                             file_pattern: str = "*.xml",
                             interval_hours: int = 24,
                             analysis_profile: str = "comprehensive") -> str:
        """Schedule a recurring batch job"""
        
        task_id = f"scheduled_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        task = {
            "task_id": task_id,
            "name": name,
            "input_directory": input_directory,
            "output_directory": output_directory,
            "file_pattern": file_pattern,
            "interval_hours": interval_hours,
            "analysis_profile": analysis_profile,
            "next_run": datetime.now(),
            "last_run": None,
            "enabled": True
        }
        
        self.scheduled_tasks[task_id] = task
        self.logger.info(f"Scheduled recurring job: {name}")
        
        return task_id
    
    def _scheduler_loop(self):
        """Background scheduler loop"""
        while self.scheduler_running:
            try:
                current_time = datetime.now()
                
                for task_id, task in self.scheduled_tasks.items():
                    if task["enabled"] and current_time >= task["next_run"]:
                        self._execute_scheduled_task(task)
                
                # Sleep for 1 minute
                time.sleep(60)
                
            except Exception as e:
                self.logger.error(f"Scheduler error: {e}")
    
    def _execute_scheduled_task(self, task: Dict[str, Any]):
        """Execute a scheduled task"""
        try:
            # Find files matching pattern
            input_dir = Path(task["input_directory"])
            if not input_dir.exists():
                self.logger.warning(f"Input directory not found: {input_dir}")
                return
            
            input_files = list(input_dir.glob(task["file_pattern"]))
            input_files = [str(f) for f in input_files if f.is_file()]
            
            if not input_files:
                self.logger.info(f"No files found for scheduled task: {task['name']}")
                return
            
            # Create batch job
            job_name = f"{task['name']} - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            job_id = self.batch_engine.create_batch_job(
                name=job_name,
                description=f"Scheduled task: {task['name']}",
                input_files=input_files,
                output_directory=task["output_directory"],
                analysis_profile=task["analysis_profile"]
            )
            
            # Update task
            task["last_run"] = datetime.now()
            task["next_run"] = task["last_run"] + threading.timedelta(hours=task["interval_hours"])
            
            self.logger.info(f"Executed scheduled task: {task['name']} (Job ID: {job_id})")
            
        except Exception as e:
            self.logger.error(f"Scheduled task execution failed: {e}")
    
    def get_scheduled_tasks(self) -> List[Dict[str, Any]]:
        """Get list of scheduled tasks"""
        return list(self.scheduled_tasks.values())
    
    def enable_task(self, task_id: str) -> bool:
        """Enable a scheduled task"""
        if task_id in self.scheduled_tasks:
            self.scheduled_tasks[task_id]["enabled"] = True
            return True
        return False
    
    def disable_task(self, task_id: str) -> bool:
        """Disable a scheduled task"""
        if task_id in self.scheduled_tasks:
            self.scheduled_tasks[task_id]["enabled"] = False
            return True
        return False
    
    def delete_task(self, task_id: str) -> bool:
        """Delete a scheduled task"""
        if task_id in self.scheduled_tasks:
            del self.scheduled_tasks[task_id]
            return True
        return False
    
    def shutdown(self):
        """Shutdown scheduler"""
        self.scheduler_running = False