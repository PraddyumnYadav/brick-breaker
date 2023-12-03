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
	# Clear the Screen
	WIN.fill((0, 0, 0))

	# Draw The Ball and Shield
	pygame.draw.circle(WIN, "red", (ball_x, ball_y), BALL_WIDTH)
	pygame.draw.rect(WIN, "white", shield)

	# Update the Display
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

	ball_vel_x = 5
	ball_vel_y = 5

	clock = pygame.time.Clock()

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		draw(shield, ball_x, ball_y)

		# Check Collision from Walls
		if ball_x+BALL_WIDTH >= WIDTH or ball_x-BALL_WIDTH <= 0:
			ball_vel_x = -ball_vel_x
		if ball_y+BALL_WIDTH >= HEIGHT or ball_y-BALL_WIDTH <= 0:
			ball_vel_y = -ball_vel_y

		# Check Collision from Shield
		if shield.colliderect(
			pygame.Rect(
				ball_x - BALL_WIDTH,
				ball_y - BALL_WIDTH,
				2 * BALL_WIDTH,
				2 * BALL_WIDTH,
			)
		):
			ball_vel_y = -ball_vel_y

		ball_x += ball_vel_x
		ball_y += ball_vel_y

		clock.tick(60)


if __name__ == "__main__":
	main()
