function average(array) {
    let sum = 0
    for (let num of array) {
        sum += num
    }
    return sum / array.length
}
var team_a_scores = [86, 73, 124, 111, 90, 38]
var team_b_scores = [84, 71, 103, 85, 90, 89]
var team_c_scores = [229, 77, 59, 95, 70, 88]
var team_a_average = average(team_a_scores)
var team_b_average = average(team_b_scores)
var team_c_average = average(team_c_scores)

console.log("The averages are: ")
console.log("Team A: " + team_a_average)
console.log("Team B: " + team_b_average)
console.log("Team C: " + team_c_average)