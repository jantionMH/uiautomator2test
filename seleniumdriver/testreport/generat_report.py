def fix_html():
    success=0
    fail=0
    with open(file='model.html', mode='r', encoding='utf-8') as f:
        re = f.read()
        re = re.replace("${version}", 'ddddd')
        re = re.replace("${machinetype}", 'android')


        with open(file='../datacneter/result.csv' ,mode='r' ,encoding='utf-8') as fcsv :
           listcsv =fcsv.readlines()
           for i in range(len(listcsv)):

               time =listcsv[i].strip().split(',')[0]
               testsense =listcsv[i].strip().split(',')[1]
               casename =listcsv[i].strip().split(',')[2]

               result=listcsv[i].strip().split(',')[3]

               screenshot=listcsv[i].strip().split(',')[4]
               reason =listcsv[i].strip().split(',')[5]

               re+= "<tr >"
               re+="<td width=5%%>%s</td\n>"%i
               re+="<td width=15%%>%s</td>\n"%time
               re+="<td width=30%%>%s</td>\n"%testsense
               re+="<td width=20%%>%s</td>\n"%casename
               if result=='测试成功':
                   success+=1
                   re += "<td bgcolor=lightgreen width=10%%>%s</td>\n" % result
               elif result=='失败':
                   fail+=1
                   re += "<td bgcolor=lightpink width=10%%>%s</td>\n" % result

               re+="<td width=10%%>%s</td>\n"%screenshot
               re+="<td width=10%%>%s</td>\n"%reason

           re = re.replace("${totalnum}", '%s'%(len(listcsv)))
           re = re.replace("${successnum}", '%s'%success)
           re = re.replace("${failnum}", '%s'%fail)
           re = re.replace("${successrate}", '{:.2%}'.format(int(success)/len(listcsv)))
           re+="</tbody></table></body></html>"
           with open(file='./repor.html', mode='w', encoding='utf-8')as ff:
                 ff.write(re)

if __name__ == '__main__':
    fix_html()
