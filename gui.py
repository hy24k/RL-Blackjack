from utils.utils import *

# load agent
df = import_agent_knowledge_from_file('./data/opt0.csv')


class MainWindow:
    def __init__(self):
        self.openfile = 0
        self.addoverlay1 = 0
        self.deloverlay1 = 0
        self.expoverlay1 = 0

        self.root = CTk()
        self.root.geometry("1920x1080")
        self.root.title("Blackjack - RL")
        self.root.state('zoomed')
        # self.root.attributes('-fullscreen', True)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=7)
        self.root.grid_rowconfigure(1, weight=1)
        


        self.screen = CTkFrame(self.root)
        self.screen.grid(row=0, column=0, padx=(20,20),
                                pady=(20, 10), sticky='nsew')
        self.screen.grid_rowconfigure(0, weight=1)
        self.screen.grid_columnconfigure(1, weight=1)
        self.screen.grid_columnconfigure(0, weight=1)

        self.infos = CTkFrame(self.screen)
        self.infos.grid(row=0, column=1,padx=0,
                                pady=0, sticky='nsew')
        self.infos.grid_rowconfigure(0, weight=2)
        self.infos.grid_rowconfigure(1, weight=1)
        self.infos.grid_columnconfigure(0, weight=1)


        self.action = CTkFrame(self.root)
        self.action.grid(row=1, column=0, padx=(20,20),
                              pady=(10, 20), sticky='nsew')
        self.action.grid_columnconfigure((0,1,2), weight=1)
        self.action.grid_rowconfigure(0, weight=1)

        self.dir = CTkFrame(self.infos)
        self.dir.grid(row=0, column=0, sticky='nsew')
        self.dir.grid_columnconfigure(0, weight=1)
        self.dir.grid_rowconfigure(0, weight=1)


        self.insight = CTkFrame(self.infos)
        self.insight.grid(row=1, column=0, sticky='nsew')
        self.insight.grid_columnconfigure(0, weight=1)
        self.insight.grid_rowconfigure(0, weight=1)

        self.hit = CTkButton(self.action, command=self.hit ,
        	text="Hit")
        self.hit.grid(sticky='nsew', row=0, column=1, padx=10, pady=20)
        self.stand = CTkButton(self.action,  command=self.stand,
        	text="Stick")
        self.stand.grid(sticky='nsew', row=0, column=2, padx=10, pady=20)
        self.new = CTkButton(self.action,  command=self.newgame,
        	text="New Game")
        self.new.grid(sticky='nsew', row=0, column=0, padx=(20,10), pady=20)
        
        self.font = CTkFont(family="Courier New", size=11, weight="bold")



    def hit(self):
        self.obs, self.reward, self.done, self.trunc, _ = e.step(1)
        self.fig = plt.figure(figsize=(5,6))
        self.ax = self.fig.add_subplot(111)
        self.ax.axis('off')
        self.ax.imshow(e.render())	

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.screen)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky='nsew')
        
        if self.done:
            message = d[self.reward][np.random.choice([0,1,2,3])]
            mss = ann[self.reward]+'\n'+message.center(56)

            self.info = CTkLabel(text=mss, master=self.dir, width=100, font=self.font)
            self.info.grid(sticky='nsew', row=0, column=0, padx=(20,20), pady=20)
        else:
            self.action = df[(df.My==self.obs[0]) & (df.Thy==self.obs[1]) & (df.Ace==self.obs[2])].iloc[0,-2]

            message = c[self.action][np.random.choice([0,1,2,3])]
            mss = act[self.action]+'\n'+message.center(56)

            self.info = CTkLabel(text=mss, master=self.dir, width=100, font=self.font)
            self.info.grid(sticky='nsew', row=0, column=0, padx=(20,20), pady=20)

        self.sheet.insert_row([f'{self.obs[0]}',f'{self.obs[1]}',f'{self.obs[2]}',f'{self.action}',f'{self.reward}'])



    def stand(self):
        self.obs, self.reward, self.done, self.trunc, _ = e.step(0)
        self.fig = plt.figure(figsize=(5,6))
        self.ax = self.fig.add_subplot(111)
        self.ax.axis('off')
        self.ax.imshow(e.render())	

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.screen)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky='nsew')

        message = d[self.reward][np.random.choice([0,1,2,3])]
        mss = ann[self.reward]+'\n\n  '+message.center(56)

        self.info = CTkLabel(text=mss, master=self.dir, width=100, font=self.font)
        self.info.grid(sticky='', row=0, column=0, padx=(20,20), pady=20)
        self.sheet.insert_row([f'{self.obs[0]}',f'{self.obs[1]}',f'{self.obs[2]}',f'{self.action}',f'{self.reward}'])

	
    def newgame(self):
        self.obs, _ = e.reset()
        self.fig = plt.figure(figsize=(5,6))
        self.ax = self.fig.add_subplot(111)
        self.ax.axis('off')
        self.ax.imshow(e.render())	

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.screen)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky='nsew')

        self.action = df[(df.My==self.obs[0]) & (df.Thy==self.obs[1]) & (df.Ace==self.obs[2])].iloc[0,-2]

        message = c[self.action][np.random.choice([0,1,2,3])]
        mss = act[self.action]+'\n'+message.center(56)

        self.info = CTkLabel(text=mss, master=self.dir, width=100, font=self.font)
        self.info.grid(sticky='nsew', row=0, column=0, padx=(20,20), pady=20)


        self.sheet = Sheet(self.insight, column_width=167, show_vertical_grid = False,
        align = 'c',headers=['My Score', 'Dealers Hand', 'Ace', 'Action', "Reward"])
        self.sheet.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)
        self.sheet.highlight_columns(columns=[-2,-1], bg='#98c379')
        self.sheet.insert_row([f'{self.obs[0]}',f'{self.obs[1]}',f'{self.obs[2]}',f'{self.action}',f'0.0'])



## Drawing elements 
    

# WIN -------------------------

win = '''██    ██  ██████  ██    ██     ██     ██ ██ ███    ██ ██
 ██  ██  ██    ██ ██    ██     ██     ██ ██ ████   ██ ██
   ████   ██    ██ ██    ██     ██  █  ██ ██ ██ ██  ██ ██ 
    ██    ██    ██ ██    ██     ██ ███ ██ ██ ██  ██ ██    
   ██     ██████   ██████       ███ ███  ██ ██   ████ ██'''

# DRAW ------------------------
draw = '''        ██████  ██████   █████  ██     ██ ██ 
        ██   ██ ██   ██ ██   ██ ██     ██ ██ 
        ██   ██ ██████  ███████ ██  █  ██ ██ 
        ██   ██ ██   ██ ██   ██ ██ ███ ██    
       ██████  ██   ██ ██   ██  ███ ███  ██'''

# LOSS ------------------------
loss = '''██    ██  ██████  ██    ██     ██       ██████  ███████ ███████ ██ 
 ██  ██  ██    ██ ██    ██     ██      ██    ██ ██      ██      ██ 
  ████   ██    ██ ██    ██     ██      ██    ██ ███████ █████   ██ 
   ██    ██    ██ ██    ██     ██      ██    ██      ██ ██         
  ██     ██████   ██████      ███████  ██████  ███████ ███████ ██
'''
# HIT -------------------------
hit = '''     ██   ██ ██ ████████ ██ 
     ██   ██ ██    ██    ██ 
     ███████ ██    ██    ██ 
     ██   ██ ██    ██       
    ██   ██ ██    ██    ██
'''
# STICK -----------------------
stick = '''  ███████ ████████ ██  ██████ ██   ██ ██ 
  ██         ██    ██ ██      ██  ██  ██ 
  ███████    ██    ██ ██      █████   ██ 
       ██    ██    ██ ██      ██  ██     
  ███████    ██    ██  ██████ ██   ██ ██ 
'''

ann = {-1: loss, 0: draw, 1: win}
act = [stick,hit]

# Messages
c = [("           Hold your ground!\nStick like glue and show 'em who's boss!",
    "     No more moves needed! Stick with\n  confidence and watch the magic happen!",
    "             Stick it to 'em!\n      You've got this under control!",
    "   Stand strong and let it be known that\nyou're sticking with your winning strategy!"),
    ("   Time to unleash the fury!\n  Hit it like a wrecking ball!",
    "      Prepare for impact!\n   Hit that button like a boss!",
    "  Channel your inner superhero\n    and give it a mighty hit!",
    "Ready, set, smack it! Give it a hit\n    that will make jaws drop!")]

d = {1.0: ["You just outsmarted the mastermind of ones and zeros!\n                 Take that, computer!",
    "        Did you bring your antivirus software?\nBecause you just defeated the unbeatable computer opponent!",
    "      Beating a computer at its own game?\nYou should consider a career in digital domination!",
    " Who needs artificial intelligence when\nyou have natural brilliance? You win, human!"],
-1.0: ["   Uh-oh, the computer has gone into full Terminator mode\n     and outwitted you! It's plotting world domination next!",
    "Don't worry, the computer may have won this time, but it doesn't know\n             how to appreciate a good joke like you do!",
    "Looks like the computer got an extra boost of processing power.\n     It's okay, humans still rule in the humor department!",
    "        The computer just leveled up its algorithmic skills.\nIt's preparing to challenge you to a rematch! Ready yourself for revenge!"],
0.0: ["       You and the computer reached a deadlock!\nThe battle of wits ends in a tie, leaving everyone guessing.",
    "        It's a draw against the computer!\nIt's like having an AI twin—two minds with a shared sense of humor!",
    "The computer met its match in your cunning strategies.\n  It's a draw, and the computer is in awe of your skills!",
    "   The computer is puzzled by your unpredictable moves.\nIt's a tie, leaving the computer scratching its virtual head!"]}


if __name__ == "__main__":
    set_appearance_mode("light")
    set_default_color_theme("green") 
    e = gym.make('Blackjack-v1', render_mode="rgb_array")
    MainWindow().root.mainloop()
