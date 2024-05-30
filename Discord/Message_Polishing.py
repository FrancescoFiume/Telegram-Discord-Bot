def Polisher(message):
    splitted = message.split("\n")

    last_line = splitted[-1]
    if "[Quoted]" in last_line or "[Replying]" in last_line or "[Retweeted]" in last_line or "[Tweeted]" in last_line:
        last_line = (last_line.split(" ")[0]
                     .replace("[Quoted]", "")
                     .replace("[Replying]", "")
                     .replace("[Retweeted]", "")
                     .replace("[Tweeted]", "")
                     .replace("(", "")
                     .replace(")", "")
                     )

    splitted[-1] = "Tweet Source: " + last_line

    message = "\n".join(splitted)
    return message