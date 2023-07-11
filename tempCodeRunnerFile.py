ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y = -ball_speed_y
    if ball.left <= 0:
        opponent_score += 1
        ball_speed_x = -ball_speed_x
    elif ball.right >= screen_width:
        player_score += 1
        ball_speed_x = -ball_speed_x