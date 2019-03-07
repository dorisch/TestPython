# Data Processing Task
## 1. How to run script
```sh
python main.py yourfile.csv
```
## 2. Supported formats
### CSV
Example:

```csv
X;Y;Z;
10;-1025;2789;
11;-978;15230;
5;-565;5456;
```
Values in column must be in range -50 000, 50 000!
### OTHER FORMATS
message:
"Unsupported data format!"
## 3. Example output
```csv
X;Y;Z;
0.0002,-0.0205,0.05578
0.00022,-0.01956,0.3046
0.0001,-0.0113,0.10912
```
