from tkinter import *
root=Tk()
root.title("Tic Tac Toe")
board=[" "]*9
game=False
def win(p):
	w=[[0,1,2],[3,4,5],[6,7,8],
	      [0,3,6],[1,4,7],[2,5,8],
	      [0,4,8],[2,4,6]]
	for i in w:
		if board[i[0]]== board[i[1]]==board[i[2]]==p:
			return True
	return False
def draw():
	return " "not in board
def minimax(ai):
	if win("O"):
		return 1
	if win("X"):
		return -1
	if draw():
		return 0
	if ai:
		best=-100
		for i in range(9):
			if board[i]== " ":
				board[i]="O"
				score=minimax(False)
				board[i]=" "
				best=max(best,score)
		return best
	else:
		best=100
		for i in range(9):
			if board[i]== " ":
				board[i]="X"
				score=minimax(True)
				board[i]=" "
				best=min(best,score)
		return best
def ai():
	bestscore=-100
	move=0
	for i in range(9):
		if board[i]== " ":
			board[i]="O"
			score=minimax(False)
			board[i]=" "
			if score>bestscore:
				bestscore=score
				move=i
	board[move]="O"
	button[move].config(text="O")
def click(i):
	global game
	if board[i]==" " and not game:
		board[i]="X"
		button[i].config(text="X")
		if win("X"):
			title["text"]="You Win!"
			game=True
			return

		if draw():
			title["text"]="Match Draw!"
			game=True

		ai()
		if win("O"):
			title["text"]="AI Win!"
			game=True
			return

title= Label(root,
		  text="Tic Tac Toe",
		  font=("Arial",25,"bold"),
		  bg="black",
		  fg="cyan")
title.grid(row=0,column=0,columnspan=3,sticky="nsew")
root.configure(bg="black")
button=[]
for i in range(9):
	b= Button(root,text=" ",
			font=("Arial",30,"bold"),	
			width=5,					
			height=2,
			bg="gray20",
			fg="white",
			bd=5,
			command=lambda i=i:click(i))
	b.grid(row=(i//3)+1,
		 column=i%3,
		 padx=5,
		 pady=5)
	button.append(b)
root.mainloop()