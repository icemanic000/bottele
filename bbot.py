from random import randint

def generate_match_results(num_matches):
    # Генерация случайных результатов матчей
    results = [randint(0, 5) for _ in range(num_matches)]
    return results

def calculate_goal_probability(team_results):
    # Расчет вероятности забитых голов для команды
    total_goals = sum(team_results)
    average_goals = total_goals / len(team_results)
    return average_goals

def main():
    # Генерация результатов для двух команд
    team1_results = generate_match_results(30)
    team2_results = generate_match_results(30)

    # Расчет вероятности забитых голов для каждой команды
    team1_goal_probability = calculate_goal_probability(team1_results)
    team2_goal_probability = calculate_goal_probability(team2_results)

    print("Вероятность забитых голов для команды 1:", team1_goal_probability)
    print("Вероятность забитых голов для команды 2:", team2_goal_probability)

if __name__ == "__main__":
    main()
