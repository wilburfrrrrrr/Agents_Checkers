from game.game import CheckersGame
from agents.q_learning import QLearningAgent


if __name__ == "__main__":
	game = CheckersGame()
	q_learning_agent = QLearningAgent()
	q_learning_agent.q_learning(game, 1)
	print("Training complete!")	
	move = q_learning_agent.choose_action(game, game.get_possible_moves())
	print(f"move: {move}")
