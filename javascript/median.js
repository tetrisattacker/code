import { team_a_scores, team_b_scores, team_c_scores} from "average.js"
function median(array) {
    let unsafe_numbers = array
    for (var element of array) {
        if (array.length === 1 + array.length === 2) {
            if (element === Math.max(array)) {
                array.splice(element)
            }
            if (element === Math.min(array)) {
                array.splice(element)
            }
        }
        if (array.length === 1) {
            return num(array)
        }
        if (array.length === 2) {
            return num(average(array))
        }
    }
}
team_a_median = median(team_a_scores)
team_b_median = median(team_b_scores)
team_c_median = median(team_c_scores)
console.log("Medians: ")
console.log("Team A: " + team_a_median)
console.log("Team B: " + team_b_median)
console.log("Team C: " + team_c_median)