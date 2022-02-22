// DEFINE YOUR FUNCTION BELOW:
function returnDay(number) {
    const daysW = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday];
    let day = number - 1;
    if (number > 7 || number < 1) {
        return null;
    }
    else return daysW[day];
}