#-- coding: utf-8 --

#@Time : 2022/7/18 13:32

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : operation_zentao_mysql.py

#@Software: PyCharm
from Utils.cennect_mysql_zentao import *
from Utils.currenttime import *
def select_zentao_sql(sql):
    """
    操作查询的sql
    sql为sql语句
    """
    connect = ConnectMysqlZentao()
    results = connect.get_select_data_zentao(sql)
    return results

def change_zentao_sql(sql):
    """
        操作修改,删除,增加的sql
        sql为sql语句
    """
    connect = ConnectMysqlZentao()
    connect.change_data_zentao(sql)


def bug_to_zentao(result,title,content,opend_by,assigned_to):
    """
    断言结果写到数据库中
    :param result: 用例断言的结果,bool类型
    :param title: bug标题
    :param content: bug内容
    :param opend_by: 创建用户
    :param assigned_to: 指派用户
    :return:
    """
    if not result:
        sql = "SELECT * from `zt_bug` WHERE title='" + title + "'"
        sql1 = "SELECT id from `zt_bug` WHERE title='" + title + "'" + "and" + " status='resolved'"
        sql2 = "SELECT id from `zt_bug` WHERE title='" + title + "'" + "and" + " status='active'"
        only_status_closed = not select_zentao_sql(sql1) and not select_zentao_sql(sql2)
        if not select_zentao_sql(sql) or only_status_closed:
            sql = "select realname from zt_user where account='"+assigned_to+"'"
            if select_zentao_sql(sql):
                sql1 = "INSERT INTO `zt_bug`(`project`, `product`, `injection`,`identify`,`branch`, `module`, `execution`, `plan`, `story`, `storyVersion`, `task`, `toTask`, `toStory`, `title`, `keywords`, `severity`, `pri`, `type`, `os`, `browser`, `hardware`, `found`, `steps`, `status`, `subStatus`, `color`, `confirmed`, `activatedCount`, `activatedDate`, `feedbackby`,`notifyEmail`,`mailto`, `openedBy`, `openedDate`, `openedBuild`, `assignedTo`, `assignedDate`, `deadline`, `resolvedBy`, `resolution`, `resolvedBuild`, `resolvedDate`, `closedBy`, `closedDate`, `duplicateBug`, `linkBug`, `case`, `caseVersion`,`feedback`, `result`, `repo`,`mr`,`entry`, `lines`, `v1`, `v2`, `repoType`,`issueKey`, `testtask`, `lastEditedBy`, `lastEditedDate`, `deleted`) VALUES (3, 1, 0, 0, 0, 2, 0, 0,0, 1, 0, 0,0, '"+title+"', '', 3, 3, 'codeerror', 'win10', '', '', '', '" + content + "', 'active', '', '', 0, 0, '0000-00-00 00:00:00', '','',',wub', '"+opend_by+"', '" + new_time() + "', 'trunk', '" + assigned_to + "', '" + new_time() + "', '0000-00-00', '', '', '', '0000-00-00 00:00:00', '', '0000-00-00 00:00:00', 0, '', 0, 0, 0, 0,0,0, '', '', '', '', '','', 0, '', '0000-00-00 00:00:00', '0')"
                # sql1 = "INSERT INTO `zt_bug`(`project`, `product`, `injection`, `identify`, `branch`, `module`, `execution`, `plan`, `story`, `storyVersion`, `task`, `toTask`, `toStory`, `title`, `keywords`, `severity`, `pri`, `type`, `os`, `browser`, `hardware`, `found`, `steps`, `status`, `subStatus`, `color`, `confirmed`, `activatedCount`, `activatedDate`, `feedbackBy`, `notifyEmail`, `mailto`, `openedBy`, `openedDate`, `openedBuild`, `assignedTo`, `assignedDate`, `deadline`, `resolvedBy`, `resolution`, `resolvedBuild`, `resolvedDate`, `closedBy`, `closedDate`, `duplicateBug`, `linkBug`, `case`, `caseVersion`, `feedback`, `result`, `repo`, `mr`, `entry`, `lines`, `v1`, `v2`, `repoType`, `issueKey`, `testtask`, `lastEditedBy`, `lastEditedDate`, `deleted`) VALUES (0, 1, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, '" + title + "', '', 3, 3, 'codeerror', 'win10', '', '', '', '" + content + "', 'active', '', '', 0, 0, '0000-00-00 00:00:00', '', '', NULL, '"+opend_by+"', '" + new_time() + "', 'trunk', '"+assigned_to+"', '" + new_time() + "', '0000-00-00', '', '', '', '0000-00-00 00:00:00', '', '0000-00-00 00:00:00', 0, '', 0, 0, 0, 0, 0, 0, '', '', '', '', '', '', 0, '', '0000-00-00 00:00:00', '0')"
                change_zentao_sql(sql1)
            else:
                sql1 = "INSERT INTO `zt_bug`(`project`, `product`, `injection`,`identify`,`branch`, `module`, `execution`, `plan`, `story`, `storyVersion`, `task`, `toTask`, `toStory`, `title`, `keywords`, `severity`, `pri`, `type`, `os`, `browser`, `hardware`, `found`, `steps`, `status`, `subStatus`, `color`, `confirmed`, `activatedCount`, `activatedDate`,`feedbackby`,`notifyEmail`,`mailto`, `openedBy`, `openedDate`, `openedBuild`, `assignedTo`, `assignedDate`, `deadline`, `resolvedBy`, `resolution`, `resolvedBuild`, `resolvedDate`, `closedBy`, `closedDate`, `duplicateBug`, `linkBug`, `case`, `caseVersion`,`feedback`, `result`, `repo`,`mr`,`entry`, `lines`, `v1`, `v2`, `repoType`,`issueKey`, `testtask`, `lastEditedBy`, `lastEditedDate`, `deleted`) VALUES (3, 1, 0, 0, 0, 2, 0, 0,0, 1, 0, 0,0, '" + title + "', '', 3, 3, 'codeerror', 'win10', '', '', '', '" + content + "', 'active', '', '', 0, 0, '0000-00-00 00:00:00','','', ',wub', '" + opend_by + "', '" + new_time() + "', 'trunk', '" + opend_by + "', '" + new_time() + "', '0000-00-00', '', '', '', '0000-00-00 00:00:00', '', '0000-00-00 00:00:00', 0, '', 0, 0, 0, 0,0,0, '', '', '', '', '','', 0, '', '0000-00-00 00:00:00', '0')"
                # sql1 = "INSERT INTO `zt_bug`(`project`, `product`, `injection`, `identify`, `branch`, `module`, `execution`, `plan`, `story`, `storyVersion`, `task`, `toTask`, `toStory`, `title`, `keywords`, `severity`, `pri`, `type`, `os`, `browser`, `hardware`, `found`, `steps`, `status`, `subStatus`, `color`, `confirmed`, `activatedCount`, `activatedDate`, `feedbackBy`, `notifyEmail`, `mailto`, `openedBy`, `openedDate`, `openedBuild`, `assignedTo`, `assignedDate`, `deadline`, `resolvedBy`, `resolution`, `resolvedBuild`, `resolvedDate`, `closedBy`, `closedDate`, `duplicateBug`, `linkBug`, `case`, `caseVersion`, `feedback`, `result`, `repo`, `mr`, `entry`, `lines`, `v1`, `v2`, `repoType`, `issueKey`, `testtask`, `lastEditedBy`, `lastEditedDate`, `deleted`) VALUES (0, 1, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, '" + title + "', '', 3, 3, 'codeerror', 'win10', '', '', '', '" + content + "', 'active', '', '', 0, 0, '0000-00-00 00:00:00', '', '', NULL, '" + opend_by + "', '" + new_time() + "', 'trunk', '" + 'libb' + "', '" + new_time() + "', '0000-00-00', '', '', '', '0000-00-00 00:00:00', '', '0000-00-00 00:00:00', 0, '', 0, 0, 0, 0, 0, 0, '', '', '', '', '', '', 0, '', '0000-00-00 00:00:00', '0')"
                change_zentao_sql(sql1)
        else:
            sql = "SELECT id from `zt_bug` WHERE title='" + title + "'" + "and" + " status='resolved'"
            if select_zentao_sql(sql):
                sql_id = str(select_zentao_sql(sql)[0][0])
                sql = "UPDATE `zt_bug` set `status`='active',`assignedDate`='" + new_time() + "',`resolvedBy`='',`resolution`='',`resolvedBuild`='',`resolvedDate`='0000-00-00 00:00:00' where id=" + sql_id
                change_zentao_sql(sql)
            else:
                pass
    else:
        sql = "SELECT id from `zt_bug` WHERE title='" + title + "'" + "and" + " status='resolved'"
        if select_zentao_sql(sql):
            sql_id = (str(select_zentao_sql(sql)[0][0]))
            sql = "UPDATE `zt_bug` set `status`='closed',`assignedTo`='closed',`assignedDate`='" + new_time() + "',`closedBy`='"+opend_by+"',`closedDate`='" + new_time() + "',`lastEditedDate`='" + new_time() + "' where id=" + sql_id
            change_zentao_sql(sql)
        else:
            sql = "SELECT id from `zt_bug` WHERE title='" + title + "'" + "and" + " status='active'"
            if select_zentao_sql(sql):
                sql_id = (str(select_zentao_sql(sql)[0][0]))
                sql = "UPDATE `zt_bug` set `status`='closed',`assignedTo`='closed',`assignedDate`='" + new_time() + "',`closedBy`='" + opend_by + "',`closedDate`='" + new_time() + "',`lastEditedDate`='" + new_time() + "' where id=" + sql_id
                change_zentao_sql(sql)


def from_zentaotitle_get_zentaoid(title):
    """
    根据禅道title获取id,取二维元祖第一个值
    :param title: 禅道bug title
    :return: id
    """
    if select_zentao_sql("SELECT id from zt_bug where title='"+title+"' and `status`= 'active'"):
        return select_zentao_sql("SELECT id from zt_bug where title='"+title+"' and `status`= 'active'")[0][0]
    else:
        return select_zentao_sql("SELECT id from zt_bug where title='"+title+"' and `status`= 'active'")