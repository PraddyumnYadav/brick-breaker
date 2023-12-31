# --------------------------Creating Classic Brick Breaker Game with Python-------------------------- #
import pygame
pygame.font.init()

# Create Global Variables
WIDTH, HEIGHT = 800, 675
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker - Praddyumn Yadav")

SHIELD_WIDTH = 250
SHIELD_HEIGHT = 25

BALL_WIDTH = 25

BRICK_WIDTH = 50
BRICK_HEIGHT = 25

BRICKS_PER_ROW = 10

FONT = pygame.font.SysFont("comicsans", 150)


def draw(shield, ball_x, ball_y, bricks, level):
	# Clear the Screen
	WIN.fill((0, 0, 0))

	# Draw Level
	level_label = FONT.render(str(level), 1, "yellow")
	WIN.blit(level_label, (WIDTH/2-level_label.get_width()/2, HEIGHT/2-level_label.get_height()/2))

	# Draw The Ball and Shield
	pygame.draw.circle(WIN, "red", (ball_x, ball_y), BALL_WIDTH)
	pygame.draw.rect(WIN, "white", shield)

	# Draw Bricks
	for brick in bricks:
		pygame.draw.rect(WIN, "blue", brick)

	# Update the Display
	pygame.display.update()


def main():
	run = True

	shield = pygame.Rect(
		int(WIDTH / 2 - SHIELD_WIDTH / 2),
		int(HEIGHT - SHIELD_HEIGHT - 25),
		SHIELD_WIDTH,
		SHIELD_HEIGHT,
	)
	shield_vel = 10

	ball_x = int(WIDTH / 2)
	ball_y = int(HEIGHT - SHIELD_HEIGHT - 50 - BALL_WIDTH)

	ball_vel_x = 5
	ball_vel_y = 5

	bricks = []
	level = 0

	clock = pygame.time.Clock()

	while run:
		if len(bricks) == 0:
			level += 1
			x = int(WIDTH / 2 - BRICK_WIDTH * 5 - 10 * 5)
			y = 50
			for _ in range(level):
				for _ in range(BRICKS_PER_ROW):
					brick = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
					x += BRICK_WIDTH + 10
					bricks.append(brick)
				# Move to the next row
				y += BRICK_HEIGHT + 10
				x = int(WIDTH / 2 - BRICK_WIDTH * 5 - 10 * 5)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		# Check Collision from Walls
		if ball_x + BALL_WIDTH >= WIDTH or ball_x - BALL_WIDTH <= 0:
			ball_vel_x = -ball_vel_x
		if ball_y + BALL_WIDTH >= HEIGHT or ball_y - BALL_WIDTH <= 0:
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

		for brick in bricks:
			if brick.colliderect(
					pygame.Rect(
						ball_x - BALL_WIDTH, ball_y - BALL_WIDTH, BALL_WIDTH, BALL_WIDTH
					)
			):
				bricks.remove(brick)
				ball_vel_y = -ball_vel_y

		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT] and not (shield.x - shield_vel < 10):
			shield.x -= shield_vel
		if keys[pygame.K_RIGHT] and not (shield.x + shield_vel > WIDTH - SHIELD_WIDTH - 10):
			shield.x += shield_vel

		ball_x += ball_vel_x
		ball_y += ball_vel_y

		draw(shield, ball_x, ball_y, bricks, level)

		clock.tick(60)


if __name__ == "__main__":
	main()
