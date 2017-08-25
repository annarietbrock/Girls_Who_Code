


def ChocoFudgeCake():
    ingredients = {"dark chocolate": "8.5oz", "caster sugar":"1 3/4 cups", "unsalted butter":"2 sticks", "milk": "1 1/4 cups", "vegetable/canola oil": "1/4 cup", "eggs": "2", "cocoa powder":"1/2 cup", "baking powder":"1 teaspoon", "plain flour":"1 3/4 cups", "coffee granules":"2 teaspoons","heavy whipping cream":"1 cup", "melted chocolate chips":"8 ounces"}

    for item, amount in ingredients.items():
        print(amount,item)
    print("")

    Cakelist = ['1. Preheat to 320F', '2. Grease a 9-10 inch spring form cake tin and line it with parchment', '3. Combine sugar, butter, and half the milk and chocolate in a saucepan in medium-low heat','4. Stir until the butter and chocolate are melted and sugar is dissolved. Do NOT let it summer or boil!','5. Pour the chocolate mixture into a bowl. Whisk in oil and remaining milk.','6. Whisk eggs in until combined','7. Sift cocoa, baking powder, flour, and coffee directly into the bowl. Whisk until smooth', '8. Pour into the cake tin and bake for 1 hour 10 minutes or until a skewer inserted into the center comes out clean.', '9. Remove sides from the cake pan and transfer it onto a cooling rack to cool']

    Ganachelist = ['1. Place chocolate in a bowl','2. Place cream in a saucepan over medium-high heat. When it is about to start simmering remove it. Do NOT let it boil!','3.Pour cream over the chocolate, shake the bowl to sumberge all of the chocolate under the cream, cover bowl with a plate, and set aside for 5 minutes','4.Stir chocolate with a spoon until smooth, refrigerate for 45 minutes to 1 hour','5. Spread over the cake, tops AND sides!','6. ENJOY! :) <3 ;)']
    print("")
    print("This is how to make the cake!")
    print("")
    for steps in Cakelist:
        print(steps)
        print("")

    print("This is how to make the ganache!")
    print("")
    for gsteps in Ganachelist:
        print(gsteps)
        print("")

def CremeBruLee():
    ingredients = {"egg yolks" : "6", "white sugar": "6 tablespoons", "vanilla extract": "1/2 teaspoon", "heavy cream": "2 1/2 cups", "brown sugar" : "2 tablespoons"}

    for item, amount in ingredients.items():
        print(amount,item)
    print("")

    CremeBruLeelist = ["1. Preheat oven to 300F", "2. Beat egg yolks, 4 tablespoons white sugar, and vanilla extract in a mixing bowl until thick and creamy", "3. Pour cream into a saucepan and stir over low heat until it almost comes to a boil, remove the cream from heat immedietly", "5.Stir cream into the egg yolk mixture and beat until combined", "6. Pour cream mixture into the top pan of the double boiler. Stir over simmering water until mixture lightly coats the back of the spoon", "7. Remove mixture from heat immedietly and pour into a shallow heat proof dish", "8. Bake for 30 minutes", "9. Remove from oven and cool to room temperature, refrigerate for at least 1 hour or overnight", "10. In a small bowl combine remaining 2 tablespoons white and brown sugar, sift this mixture evenly over custard. Place dish under boiler until sugar melts", "11. Remove from heat, allow to cool. refrigerate until custard is set again"]

    print("This is how to make creme brulee!")
    print("")
    for steps in CremeBruLeelist:
        print(steps)
        print("")

print("Would you like to know how to make creme brulee or chocolate fudge cake?")
input_choice = input()

if input_choice == "chocolate fudge cake":
    ChocoFudgeCake()

if input_choice == "creme brulee":
    CremeBruLee()
