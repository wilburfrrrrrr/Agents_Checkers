from game.game import CheckersGame
from agents.deep_learning import DeepLearningAgent

if __name__ == "__main__":
	game = CheckersGame()
	deep_learning_agent = DeepLearningAgent()
	deep_learning_agent.compile()
	deep_learning_agent.train(game, 1)
	print("Training complete!")
	move = deep_learning_agent.select_move(game)
	print(f"move: {move}")
