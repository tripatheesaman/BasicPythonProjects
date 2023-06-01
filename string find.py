data = 'From stepher.ramshyam@lolomegalol.gg.com sat jan 5 00:08:13 2009'
at_find = data.find('@')
end_find = data.find('.gg')
necessary_word = data[at_find+1:end_find]
necessary_word = necessary_word.strip()
print('Lol you got it', necessary_word)
