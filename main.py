import pandas as pd
import requests


if __name__ == '__main__':
    # TODO 替换Cookie，通过浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68',
        'Cookie': '',
    }

    # TODO 替换csrfKey、termId，通过浏览器
    csrfKey = ''
    termId = 000000
    # TODO 可选替换，resultName，保存的结果文件名
    resultName = 'result'

    url = 'http://www.icourse163.org/mm-tiku/web/j/mocTermScoreSummaryRpcBean.getStudentScorePagination.rpc?csrfKey={}'.format(csrfKey)

    param = {
        'termId': termId,
        'pIndex': 1,
        'pSize': 20,
        'rangeType': 1,
        'groupId': -1,
        'sort': 12,
        'searchName': ''
    }

    result = requests.post(url=url, data=param, headers=headers).json()

    queryInfo = result['result']['query']

    totlePageCount = queryInfo['totlePageCount']

    print('总学生数{}'.format(queryInfo['totleCount']))
    print('总页数{}'.format(totlePageCount))

    resultDf = pd.DataFrame(columns=['学号', '姓名', '测试', '作业', '考试', '新版考试', '课堂讨论', '域外成绩', '成绩'])

    resultDf.to_csv('{}.csv'.format(resultName), index=False, encoding='ANSI')
    print('开始爬取。。。')
    for index in range(1, totlePageCount + 1):
        params = {
            'termId': termId,
            'pIndex': index,
            'pSize': 20,
            'rangeType': 1,
            'groupId': -1,
            'sort': 12,
            'searchName': ''
        }

        result2 = requests.post(url=url, data=params, headers=headers).json()

        students = result2['result']['list']

        for student in students:
            school = student['schoolName']
            if school != '武汉理工大学':
                continue

            # 学号
            id = student['studentNumber']
            # 姓名
            name = student['realName']
            # 测验
            testScore = student['testScore']
            # 作业
            assignmentScore = student['assignmentScore']
            # 考试
            examScore = student['examScore']
            # 新版考试
            newExamScore = student['newExamScore']
            # 课堂讨论
            replyVote = '{}\{}'.format(student['replyCount'], student['voteCount'])
            # 域外成绩
            outsideScore = student['outsideScore']
            # 成绩
            totalScore = student['totalScore']

            df = pd.DataFrame([[id, name, testScore, assignmentScore, examScore, newExamScore, replyVote, outsideScore, totalScore]])
            df.iloc[:, 6] = df.iloc[:, 6].astype(str)

            df.to_csv('{}.csv'.format(resultName), index=False, header=None, mode='a', encoding='ANSI')

    print('爬取完成！')
