# Calculator
My secondary school project, based on Python and the Qt framework. 

Includes an exe file with a modified second version of the project, the implementation of which has been lost.
# Features
* Basic arithmetic operations:

  * Addition (+)
  * Subtraction (−)
  * Multiplication (×)
  * Division (/)
* Decimal number support
* Error handling:

  * Division by zero
  * Undefined results (e.g. 0/0)
* Negation (±)
* Backspace support
* Adaptive font size based on input length
* Additional window for equations
* Keyboard input

# Interface

The calculator is implemented using PyQt5 and includes:

* Input field (`QLineEdit`)
* Expression display (`QLabel`)
* Digit and operation buttons
* Dynamic text resizing


# Technologies

* Python 3
* PyQt5


# Installation & Run

### 1. Clone the repository

```bash
git clone https://github.com/Nyf-Nyf7/Calc.git
cd Calc-main
```

### 2. Install dependencies

```bash
pip install PyQt5
```

### 3. Run the application

```bash
python main.py
```


# Project Structure

```
.
├── main.py           # main application file
├── design.py        # UI layout (generated with Qt Designer)
├── secwin.py         # secondary window (Equations)
├── fonts/            # custom fonts (Rubik)
└── README.md
```

# License

The Unlicense
