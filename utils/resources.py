GENERAL_SCRIPT_PATH = os.path.join(SCRIPT_DIR, 'general.json')


general_script, script, memory_inputs= setup(GENERAL_SCRIPT_PATH, SCRIPT_PATH)

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to format resource links
rsrc_str = "Here are some links I found that may be useful to the issues you are having:\n"
rsrc_str_l = rsrc_str.lower()

 
response = generate_response(rsrc_str, script, general_script['issues'], memory_stack, memory_inputs)
 
# to search
query = JSON.stringify(general_script['issues'])
 
for j in search(query, tld="co.in", num=2, start=1, stop=2, pause=2):
    print(j)