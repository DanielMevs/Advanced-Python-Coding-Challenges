from collections import deque


def html2markdown(html):
    '''Take in html text as input and return markdown'''

    html = html.replace('\n', ' ')
    if '<em>' or '</em>' in html:
        html = html.replace('<em>', '*').replace('</em>', '*')
    
    html = replaceConsecutiveSpaces(html)
    html = replaceParagraphTags(html)
    html = getHtmlToMd(html)

    return html


def getHtmlToMd(urlStr):
    urls = getUrls(urlStr)
    phrases = getPhrases(urlStr)
    linksAndPhrases = list(zip(urls, phrases))
    formatted_urls = getFormattedUrs(linksAndPhrases)
    prefixAndSuffix = getPrefixAndSuffix(urlStr)
    result = convertToMd(formatted_urls, prefixAndSuffix)
    
    return result


def getConsecutiveSpaces(phrase):
    result = {}
    i = 1
    while i < len(phrase):
        runSum = 0
        prev = phrase[i - 1]
        temp = i
        while i < len(phrase) and prev == ' ' and phrase[i] == ' ':
            runSum += 1
            i += 1
        if runSum > 1:
            result[temp] = runSum
        
        i += 1
    
    return result


def replaceParagraphTags(phrase):
    phrase = phrase.replace('</p><p>', '\n\n')
    phrase = phrase.replace('<p>', '').replace('</p>', '')
    return phrase
    

def replaceConsecutiveSpaces(phrase):
    skipIndices = getConsecutiveSpaces(phrase)
    print(skipIndices)
    i = 0
    result = ''
    while i < len(phrase):
        if i in skipIndices:
            i += skipIndices[i]
        result += phrase[i]
        i += 1
    return result


def getUrls(link):
    result = []
    links = link.split('<a href="')
    
    for link in links:
        if 'https' in link:
            url = link.split('">')[0]
            result.append(url)
    return result


def getPhrases(link):
    result = []
    temp = link.split('</a>')

    for s in temp:
        if 'http' in s:
            result.append(s.split('>')[-1])

    return result


def getPrefixAndSuffix(link):
    result = deque()
    temp = link.split('</a>')
    for s in temp:
        if 'http' in s:
            result.append(s.split('<a')[0])
        else:
            result.append(s)

    return result


def formatUrlToMd(url: str, phrase: str) -> str:
    return f'[{phrase}]({url})'    


def getFormattedUrs(linksAndPhrases: list[tuple]) -> deque[str]:
    result = deque()
    
    for url, phrase in linksAndPhrases:
        result.append(formatUrlToMd(url, phrase))
    
    return result


def convertToMd(urls, fillers):
    result = ''
    while urls or fillers:
        if fillers:
            result += fillers.popleft()
        if urls:
            result += urls.popleft()
    
    return result
        

   