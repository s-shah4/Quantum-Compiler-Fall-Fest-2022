import numpy as np

q0=np.array([[1],[0]])
q1=np.array([[0],[1]])

X_gate = np.array([[0, 1], [1, 0]])
Y_gate = np.array([[0, -1j], [1j, 0]])
Z_gate = np.array([[1, 0], [0, -1]])
H_gate = np.array([[1, 1], [1, -1]])*(1/np.sqrt(2))
CNOT_gate = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])

def apply_gate(qubit, gate):
    return np.matmul(gate, qubit)

print("Do you want to change the initial state? (y/n)")
choice = input()
if choice == 'y':
    print("Enter the initial state: \n q0=")
    q00 = complex(input())
    q01 = complex(input())
    print("q1=")
    q10 = complex(input())
    q11 = complex(input())
    q0 = np.array([[q00], [q01]])
    q1 = np.array([[q10], [q11]])
elif choice == 'n':
    pass
else:
    print("Invalid Input")

print("On which qubit do you want to apply a gate? (q0, q1, q0q0, q0q1, q1q0 q1q1)")
uinp=input()
if(uinp=='q0'):qubit=q0
elif(uinp=='q1'):qubit=q1
elif(uinp=='q0q0'):qubit=np.kron(q0,q0)
elif(uinp=='q0q1'):qubit=np.kron(q0,q1)
elif(uinp=='q1q0'):qubit=np.kron(q1,q0)
elif(uinp=='q1q1'):qubit=np.kron(q1,q1)
else:print("Invalid Input")

print("Which gate do you want to apply? (X, Y, Z, H, CNOT)")
gate = input()
if gate == 'X':
    print(apply_gate(qubit,X_gate))
elif gate == 'Y':
    print(apply_gate(qubit,Y_gate))
elif gate == 'Z':
    print(apply_gate(qubit,Z_gate))
elif gate == 'H':
    print(apply_gate(qubit,H_gate))
elif gate == "CNOT":
    print(apply_gate(qubit,CNOT_gate))
else:
    print("Invalid Input")
