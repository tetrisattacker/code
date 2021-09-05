beakers = 20
tubes = 30
rubber_gloves = 10
safety_glasses = 4
enough_safety_glasses = (safety_glasses % 4) == 0
enough_rubber_gloves = rubber_gloves >= (2 * 4)
enough_tubes = tubes >= 10 * 4
enough_beakers = beakers >= 5 * 4

final_report = f'''
Here is the final report for lab materials:
-
Each girl had enough safety glasses: {enough_safety_glasses}
Each girl had enough rubber gloves: {enough_rubber_gloves}
Each girl had enough tubes: {enough_tubes}
Each girl had enough beakers: {enough_beakers}
-
There are enough gloves and safety glasses for each girl:
{enough_rubber_gloves and enough_safety_glasses}
There are more than enough tubes and an exact amount of beakers for each girl:
{tubes > 40 and beakers == 20}
Each girl has at least the exact amount or greater amount of tubes or the exact amount of beakers:
{tubes >= 40 or beakers == 20}
'''
print(final_report)