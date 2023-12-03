# --------------------------Creating Classic Brick Breaker Game with Python-------------------------- #
import pygame

# Create Global Variables
WIDTH, HEIGHT = 800, 675
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker - Praddyumn Yadav")

SHIELD_WIDTH = 250
SHIELD_HEIGHT = 25

BALL_WIDTH = 25


def draw(shield, ball_x, ball_y):
	pygame.draw.circle(WIN, "red", (ball_x, ball_y), BALL_WIDTH)
	pygame.draw.rect(WIN, "white", shield)
	pygame.display.update()


def main():
	run = True

	shield = pygame.Rect(
		int(WIDTH / 2 - SHIELD_WIDTH / 2),
		int(HEIGHT - SHIELD_HEIGHT - 50),
		SHIELD_WIDTH,
		SHIELD_HEIGHT
	)

	ball_x = int(WIDTH/2)
	ball_y = int(HEIGHT - SHIELD_HEIGHT - 50 - BALL_WIDTH)

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		draw(shield, ball_x, ball_y)


if __name__ == "__main__":
	main()
