import runpod

def handler(job):
    """
    """
    job_input = job.get("input", {})
    job_id = job.get("id", "no-id-found")
    
    print(f"MOCK_LOG: Received job {job_id}")
    
    return {
        "status": "success",
        "message": "The infrastructure is working perfectly.",
        "received_data": job_input,
        "proxy_check": "passed"
    }

if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})