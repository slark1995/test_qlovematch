from django.db import models
from datetime import date


# Create your models here.
# 用户表
class User1(models.Model):
    union_id = models.CharField(max_length=32, verbose_name='微信uid', default='', unique=True)
    open_id = models.CharField(max_length=128, verbose_name='微信open_id', default='', unique=True)
    avatar_url = models.URLField(verbose_name='头像地址', max_length=256, default='', blank=True)
    nickname = models.CharField(max_length=32, verbose_name='微信昵称', default='', blank=True)

    user_sex = models.BooleanField(default=0, verbose_name='性别', help_text='0女1男')
    user_birthday = models.DateTimeField(verbose_name='用户生日', default=0, blank=True)
    user_phone = models.CharField(verbose_name='电话', max_length=11, null=True, blank=True)
    user_address = models.IntegerField(verbose_name='用户地址', default=1)
    user_privacy = models.BooleanField(verbose_name='隐私设置', default=0, help_text='0不设置电话保护，1设置电话保护')

    user_truth = models.BooleanField(verbose_name='认证状态', default=0, help_text='0未认证，1已认证')
    create_time = models.DateTimeField(verbose_name='注册时间', auto_now_add=True)
    user_times = models.SmallIntegerField(verbose_name='剩余使用次数', default=3)

    @property
    def is_authenticated(self):
        return True

    class Meta:
        verbose_name = '恋爱速配用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}——{1}'.format(self.id, self.open_id)


# 题库名表
class QuestionBank(models.Model):
    qb_name = models.CharField(verbose_name='题目种类', max_length=64, unique=True, blank=True)
    qb_no = models.SmallIntegerField(verbose_name='排序', unique=True, blank=True)
    qb_state = models.BooleanField(verbose_name='题库状态', default=0, help_text='0开启1关闭')
    qb_price = models.SmallIntegerField(verbose_name='匹配价格', default=18, blank=True)
    qb_num = models.IntegerField(verbose_name='匹配显示数量', default=0, blank=True)
    qb_picture = models.URLField(verbose_name='图片', max_length=256, blank=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    is_open = models.BooleanField(verbose_name='点击路径', default=0, help_text='0匹配1组队')  # 直接匹配或进入组队页面

    class Meta:
        verbose_name = '题目种类'
        verbose_name_plural = verbose_name


# 题库数据表
class QuestionBankData(models.Model):
    qb_id = models.SmallIntegerField(verbose_name='题目种类', blank=True, unique=True)
    yesterday_user_login_number = models.IntegerField(verbose_name='昨日登录人数', default=0, blank=True)
    all_login_number = models.IntegerField(verbose_name='总登录人数', default=0, blank=True)
    yesterday_user_done_number = models.IntegerField(verbose_name='昨日完成人数', default=0, blank=True)
    all_done_number = models.IntegerField(verbose_name='总完成次数', default=0, blank=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '题库种类数据'
        verbose_name_plural = verbose_name


# 题目表
class Question(models.Model):
    qb_id = models.SmallIntegerField(verbose_name='题目种类', unique=0, blank=True)
    question = models.CharField(verbose_name='题目', max_length=128, blank=True)
    answer1 = models.CharField(verbose_name='答案1', max_length=128, blank=True)
    answer2 = models.CharField(verbose_name='答案2', max_length=128, blank=True)
    answer3 = models.CharField(verbose_name='答案3', max_length=128, blank=True)
    answer4 = models.CharField(verbose_name='答案4', max_length=128, blank=True)
    is_open = models.BooleanField(verbose_name='开启状态', default=0, help_text='0开启1关闭')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '题目'
        verbose_name_plural = verbose_name


# 匹配记录表
class MatchRecordTable(models.Model):
    match_choice = (
        ('匹配中离开', 0),
        ('匹配失败', 1),
        ('答题中离开', 2),
        ('匹配成功', 3),
    )
    initiator_id = models.IntegerField(verbose_name='发起者ID', blank=True)
    all_match_user = models.CharField(verbose_name='所有匹配用户ID', max_length=128)
    match_user = models.IntegerField(verbose_name='成功匹配用户ID', blank=True)
    db_id = models.SmallIntegerField(verbose_name='题库名ID', default=0, blank=True)
    match_create_time = models.DateTimeField(verbose_name='匹配发起时间', auto_now_add=True)
    answer_start_time = models.DateTimeField(verbose_name='开始答题时间', null=True)
    match_state = models.SmallIntegerField(verbose_name='匹配状态', default=0,choices=match_choice)
    match_end_time = models.DateTimeField(verbose_name='匹配成功时间', null=True)
    user_share = models.BooleanField(verbose_name='用户是否分享', default=0, help_text='0不分享，1分享')

    class Meta:
        verbose_name = '匹配记录'
        verbose_name_plural = verbose_name


# 用户答案表
class Answer(models.Model):
    user_id = models.IntegerField(verbose_name='用户ID', blank=True, null=True)
    question_id = models.IntegerField(verbose_name='题目ID', blank=True, null=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True, blank=True)
    answer = models.SmallIntegerField(verbose_name='答案', default=-1, help_text='-1为未答题', null=True)
    mrt_id = models.IntegerField(verbose_name='匹配场次记录ID', null=True)

    class Meta:
        verbose_name = '答案记录'
        verbose_name_plural = verbose_name


# 用户登录记录表
class Login(models.Model):
    user_id = models.IntegerField(verbose_name='用户ID', blank=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    login_day = models.SmallIntegerField(verbose_name='登录天数', unique=1)

    class Meta:
        verbose_name = '登录记录'
        verbose_name_plural = verbose_name


# 邀请认证表
class Invitation(models.Model):
    initiator_id = models.IntegerField(verbose_name='发起邀请用户ID', blank=True, null=True)
    recipient_id = models.IntegerField(verbose_name='接受邀请用户ID', blank=True, null=True)
    create_time = models.DateTimeField(verbose_name='分享时间', auto_now_add=True)
    db_share_id = models.SmallIntegerField(verbose_name='分享项目', blank=True, null=True)

    class Meta:
        verbose_name = '邀请登记表'
        verbose_name_plural = verbose_name


# 用户行为表
class Action(models.Model):
    action_type_choice = (
        ('分享行为', 1),
        ('点击行为', 2),
        ('页面访问行为', 3),
    )
    action_choice = (
        ('邀请认证', 101), ('邀请组队', 102), ('查看信息', 103), ('添加联系方式', 104),

        ('主页快速匹配按钮', 201), ('主页恋爱资料卡', 202), ('主页开始匹配按钮', 203), ('确认与你门当户对的他错过窗口', 204),
        ('匹配失败页面再来一轮按钮点击', 205), ('匹配成功页面继续匹配按钮点击', 206), ('匹配失败页面尝试同城按钮', 207),

        ('主页', 301), ('恋爱资料卡', 302), ('付费等待页面', 303), ('认证页面', 304),
        ('等待匹配页面', 305), ('答题页面', 306), ('结果页面', 307),
    )
    user_id = models.IntegerField(verbose_name='用户id', blank=True, null=True)
    create_time = models.DateTimeField(verbose_name='行为发生时间', auto_now=True)
    action_type = models.SmallIntegerField(verbose_name='行为类型', default=1, choices=action_type_choice)
    action = models.SmallIntegerField(verbose_name='行为', default=101, choices=action_choice)

    class Meta:
        verbose_name = '行为'
        verbose_name_plural = verbose_name


# 用户表
class ShareAction(models.Model):
    action_id = models.SmallIntegerField(verbose_name='用户行为表ID', blank=True)
    new_user_id = models.IntegerField(verbose_name='新用户ID', blank=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '接受分享行为'
        verbose_name_plural = verbose_name
