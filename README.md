\# 🤖 Agentic AI Lab (Day 1 – Day 4)



\## 📌 Overview



This repository contains a step-by-step implementation of \*\*Agentic AI systems\*\*, developed as part of a Software Lab.

The project demonstrates the evolution of AI agents from simple rule-based systems to advanced multi-step planning agents.



\---



\## 🎯 Objectives



\* Understand AI agent architecture

\* Build rule-based and tool-using agents

\* Implement decision-making systems

\* Simulate LLM-based reasoning

\* Design multi-step planning agents



\---



\# 📅 Day 1: Rule-Based AI Agent



\## 🔹 Description



A simple AI agent built using \*\*rule-based logic (if-else conditions)\*\*.



\## 🔹 Features



\* Takes user input

\* Identifies intent using keywords

\* Performs actions accordingly



\## 🔹 Example



```

Input: hello  

Output: Hello! How can I help you?

```



\---



\# 📅 Day 2: Tool-Using Agent



\## 🔹 Description



An agent that uses \*\*external tools/functions\*\* to perform tasks.



\## 🔹 Tools Implemented



\* Calculator

\* Weather (mock data)

\* Text Summarizer



\## 🔹 Workflow



```

Input → Decision Logic → Tool Selection → Execution → Output

```



\---



\# 📅 Day 3: LLM-Based Agent (Simulated)



\## 🔹 Description



Replaces rule-based decision-making with \*\*LLM-style reasoning\*\*.



\## 🔹 Key Points



\* LLM decision-making is \*\*simulated\*\* using logic

\* No API used (as allowed in assignment)

\* Dynamic tool selection

\* Logging implemented



\## 🔹 Workflow



```

Input → Simulated LLM → Tool Selection → Output → Logging

```



\## 🔹 Logging Example



```

INPUT: calculate 5+5  

TOOL: calculator  

OUTPUT: 10  

\----------------------------------------

```



\---



\# 📅 Day 4: Multi-Step Agent (Planning Agent)



\## 🔹 Description



An advanced agent that can \*\*break down complex tasks into multiple steps\*\* and execute them sequentially.



\## 🔹 Features



\* Step planning

\* Sequential execution

\* Intermediate outputs

\* Supports multiple operations



\## 🔹 Supported Operations



\* Sum

\* Average

\* Maximum

\* Minimum

\* Summarization



\## 🔹 Workflow



```

Input → Step Planning → Execution → Intermediate Outputs → Final Result

```



\## 🔹 Example



```

Input:

Find average of 10, 20, 30 and summarize



Output:

\[Step 1] Extracted numbers: \[10, 20, 30]

\[Step 2] Calculated average: 20.0

\[Step 3] Summary: The result is 20.0, which represents the computed value.

```



\---



\## 🏗️ Project Structure



```

agentic-ai-lab/

│

├── day1/

├── day2/

├── day3/

├── day4/

│

└── README.md

```



\---



\## ⚙️ Requirements



\* Python 3.x

\* pip

\* Git



\---



\## ▶️ How to Run



1\. Navigate to any day folder:



```

cd day3

```



2\. Run the program:



```

python main.py

```



\---



\## 🚪 Exit Condition



To stop the program, type:



```

exit

```



\---



\## 📝 Logging



The system maintains logs including:



\* User input

\* Selected tool / steps

\* Output



Logs are stored in:



```

logs.txt

```



\---



\## 🎓 Learning Outcomes



\* AI agent workflows

\* Tool integration

\* Decision-making systems

\* Sequential reasoning

\* Planning-based AI design



\---



\## 📌 Conclusion



This project demonstrates the progression of AI systems from:



\* Simple rule-based agents

&#x20; ➡️ Tool-integrated agents

&#x20; ➡️ LLM-based decision systems

&#x20; ➡️ Multi-step planning agents



\---



\## 👩‍💻 Author



\*\*Name:\*\* Supraja

\*\*Course:\*\* Software Lab – Agentic AI



