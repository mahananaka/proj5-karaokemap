"""
Processes point of enterests from data file for map makers
"""

def process(raw):
    """
    Line by line processing of syllabus file.  Each line that needs
    processing is preceded by 'head: ' for some string 'head'.  Lines
    may be continued if they don't contain ':'.  If # is the first
    non-blank character on a line, it is a comment ad skipped. 
    """
    entry = { }
    cooked = [ ]

    for line in raw:
        line = line.strip()
        if len(line) == 0 or line[0]=="#" :
            continue
        parts = line.split(';')
        if len(parts) == 3:
            entry["description"] = parts[0].strip()
            entry["long"] = parts[1].strip()
            entry["lat"] = parts[2].strip()
            cooked.append(entry)
            entry = { }
            continue
        else:
            raise ValueError("Trouble wiht line: '{}'\n".format(line))
            field = parts[0]
            content = parts[1]
        
    return cooked

def main():
    f = open("data/poimarkers.txt")
    parsed = process(f)
    print(parsed)

if __name__ == "__main__":
    main()

    
    
            
    
