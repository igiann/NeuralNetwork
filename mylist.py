from m3u_parser import M3uParser
url = "tv_channels_6003680689_plus.m3u"
useragent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
parser = M3uParser(timeout=5, useragent=useragent)
parser.parse_m3u(url)
#parser.remove_by_extension('mp4')
parser.retrieve_by_category('EU | GREECE ΓΕΝΙΚΑ')
#parser.filter_by('status', 'GOOD')
#print(len(parser.get_list()))
parser.to_file('test1.m3u')
