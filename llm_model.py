import os
import google.generativeai as genai

# Step 1: Set your API key securely
# The script will read your API key from an environment variable named "GOOGLE_API_KEY".
try:
    genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
except Exception as e:
    print(f"Failed to configure Google API client: {e}")
    print("Please ensure the GOOGLE_API_KEY environment variable is set correctly.")
    exit()

# Step 2: Define your prompts with the error logs
error_log_gpl = """
[ERROR GPL-0302] Use a higher -density or re-floorplan with a larger core area.
Given target density: 0.75
Suggested target density: 0.87
Error: gpl.tcl, 71 GPL-0302
child process exited abnormally
"""

error_log_dpl = """
[INFO DPL-0034] Detailed placement failed on the following 1 instances:
[INFO DPL-0035] input29
[ERROR DPL-0036] Detailed placement failed.
Error: groute.tcl, 42 DPL-0036
child process exited abnormally
"""

error_log_grt = """
[ERROR GRT-0010] No routing tracks available.
Error: groute.tcl, 54 GRT-0010
child process exited abnormally
"""

error_log_cts = """
[ERROR CTS-0010] Clock skew constraint violated for net clk.
Max skew limit: 0.150ns. Actual skew: 0.235ns.
Error: cts.tcl, 30 CTS-0010
child process exited abnormally
"""

# Combine all error logs into a single prompt for the LLM
prompt = f"""Explain the following four VLSI error logs in a simple sentence and suggest a fix for each.

Error Log 1 (Placement):
{error_log_gpl}

Error Log 2 (Placement):
{error_log_dpl}

Error Log 3 (Routing):
{error_log_grt}

Error Log 4 (CTS):
{error_log_cts}
"""

# Step 3: Run the chat completion with a specific model
try:
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    
    # Step 4: Print the result
    print("--- Gemini LLM Analysis ---")
    print(response.text)

except Exception as e:
    print(f"Error with Google Gemini API: {e}")
    print("API call failed. Please double-check your API key and network connection.")
