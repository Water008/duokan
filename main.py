#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
@File      : duokan.py
@Time      : 2021-03-25 11:18:10
@Author    : Water
@Software  : Visual Studio Code
"""

import os
import re
import time
import requests


class DuoKan:
    signcodes = [
        "d16ad58199c69518a4afd87b5cf0fe67",
        "828672d6bc39ccd25e1f6ad34e00b86c",
        "f0ccc1bb1cecea673c197b928fb8dbd9",
        "6b86c490d92a138de9a0ae6847781caa",
        "c707047e8b820ba441d29cf87dff341e",
        "82b2c012a956b18cff2388d24f2574a6",
        "87d6b5183a361ee1f6ea8cece1ee83c3",
        "9d42576f7e99c94bb752fde06e6770a5",
        "e58d1f67a82a539d9331baaa3785a943",
        "52c95192ebcb1d0113a748df58a72055",
        "511f33e481fe4504d2637aaf6cbbbaff",
        "6e986f36f4a45cadf61d2f246b27cdc6",
        "f27797a6a1d7fe495b0f4de05f799327",
        "4bd335e899fa665f15eea2f215156321",
        "9355df762183f084473432b5c6900c44",
        "4fb21fb04cbbae9d65556c3958603674",
        "2d02ceb4f1bc916510c7407ce4eca5a5",
        "ef314bf665af0b51294e624244acd7d6",
        "1b441a2ab8e9e7dcf11a55b85931132f",
        "005d2345782ab456e5af167336b70623",
        "51ac508a4d494654035f17f1d646779b",
        "0f6579670f1081f1bcba89dd64645b48",
        "0cd858abe26f0d3db561185fe26bbb75",
        "b5f5fd5b47fd587cb003807e97bed783",
        "6ac9509a5cb799efeb1bb877c505f7e3",
        "b5dd986ffc84762429901ffe633d82a0",
        "f98a436cc2c85943d23d986a8d84c3bd",
        "6fc387f2a17b8564ca212e2b16544cc3",
        "12ead6a62411402378c6311199a0b2ef",
        "7d8dcf31e2e69fcf6bd8af4f48831e92",
        "446c3d0303b0dbd6bc2157844f1222ad",
        "439890227d823ff57bed8ad351fa1b75",
        "645acf3107722ab26b9d3194ecd156ff",
        "afcb41dd9bc54d752c26ace985b49960",
        "1100ab94ccd2e8373af70326c194d8ea",
        "373d73c0c0975cf959eb4c40dc82b27c",
        "2167ac28833149e9ad4ca217bcfa1a62",
        "80547afccc42f34e4c8c4083e00a41a6",
        "b604dda473644bd8157bafdf4ae518dc",
        "15eaa8f727b595d512b82f55364b53b9",
        "8fb656937fd613ccbbcacdc384595b03",
        "dd8410da0b5144ba4aba5a618723b72e",
        "204208386b056a2288e541110bfeeec3",
        "c5b2e7344efd4128bcab5840fa427103",
        "0168601e4335095c502e2e550ca53114",
        "dfa12fe056a8deee35da18613173560f",
        "ed945efdef9c7b2de41249a4fed3945e",
        "b9ece5964ab62d51f8b70ffd35191e9d",
        "f0e0ca4ca0b8afd766821a4922a2873c",
        "5c687b8c6bd641f3f2c0d6aaeceafff6",
        "c983be6420027231d77b748f9d02c1f2",
        "7c53358df8156d979cb6cbb74e15877b",
        "a58058035f73628a7c0847c66c350e88",
        "79dd039ca5cf401993801710f9900d6b",
        "5aff116c2cec01fcc69b389034f456a2",
        "d006927cd9bfd620a6af4f76ee3c4100",
        "410fe62830eeb91ca48be24ffe596364",
        "9d18226ff144a72812d0104ce59fb34e",
        "de439c7f75ca80b1d5b8aba619ee200d",
        "00d1a0479590793294bfdd5c427643aa",
        "d57176b1ce88135243bd501e448b8559",
        "7c500eff681637b97dd526bb11737abb",
        "3e197e47aaac926ccd50c37eb2828311",
        "7db084ea5987f841ad77240bcbb8ce54",
        "cce74f0facc50d47c0dd0e3e2f7435fb",
        "f8bb53fbeb9b2d45db8aca1401817599",
        "5baf7f0f355db11eeb0e936b675cdb82",
        "4478a3354de6bcd7e91b49e28a2b2b3f",
        "66a0338d93af82e956122288b08d2b4b",
        "9f598b2b1c9cd0f2b20e335831cce366",
        "9f4a45fec88b2820653abba179759eb6",
        "41086649c9a39ec977ba42f9ce81f828",
        "06ccca6fd73a6e38f65638ab8abbab76",
        "0cfa0a034a203bb3a22be499e74906f4",
        "c0d1da35a8878b7e4dcdf44bf3cd6b96",
        "f34921e16f6518c1149cc083bd8e1ad7",
        "ed0be3c70075d1d8f1a412f9e59a12e7",
        "eb4d6324bae7db952bd220cb4d57a3de",
        "5ba65d9f8ad735681b594f5092f6ab37",
        "2fa6e0b612962937edb37ed7043923fd",
        "baa8268c7d85d793011c5f5b977f8d4b",
        "f4842a465e4583646abf7df67d8e2915",
        "12c6332c8c9ded3d58d45f2dae7de8da",
        "f56609232205692acf6b6a5d337b0965",
        "3e4eed15387843c668fba53641599d07",
        "d1b9d9ede145b5d426130986245cb66e",
        "2979e43f6ab786f5d68cc262105f3c45",
        "118a18ed578c78f4855b416f8271b29a",
        "9122e158d034f094627c70ed6c3d0c33",
        "dd5413c17253e86cc4247984f3bb77e5",
        "b36bb0124b962efccbb601486665ce9e",
        "6afb3a719f8b0a0b2f744b3dad8b15ab",
        "faf18d64268402ed2975a3f60bc9e651",
        "9f4081944d4ca3fa7b831d7c3b6c289d",
        "367d7a3d77a9f96cbd7903b33c30b61f",
        "605276cf621ff9ba34a99e3675a006f6",
        "a50a734c1a3a749918e20205505ef91d",
        "271ff14ba5edfe89a80a3430227bc11b",
        "3bae338062b4bb3a5087eb13cbcc6efe",
        "9b443d60178a9bcb08bae62c41970abf",
        "a4f6e97741054f3567ab6a7257c63ab1",
        "e06a82cc1f05eda4947e5fa0927d89c5",
        "4fa3b4fc274c283efb02c0a1ddd133e7",
        "4aa59e16a3961ed1ebd12b7f15d79547",
        "f75fe88eaa24fc28ac57d963d8b90f2d",
        "42cbe52b6f74761a5a7a79bf370c30ef",
        "7d4571b5c9710e3b5481330bc7123ecc",
        "fcf2f7ec42086809991de5aed5e7ef0d",
        "bb7de9aaf68a83ac1ddbe75ba913b8af",
        "a9bd964b97e785fffb641edb9b402d3f",
        "6a815be6f537b2351e947ed66f74e209",
        "27ae4e4d71395c6255bf7ea57c496507",
        "2b07f369e90f4fc34ef419d891a2906f",
        "7a2dc8a5b3fc0c7ecddb97ed1ce2c833",
        "e7ad152ef27beb80c5d343f41f885b21",
        "ba21758aed15a3a20a27f63bc0d84626",
        "3820f7b8e1ece2614a11264501b5c93e",
        "c3c41c87e6bf752f5237b4fffa33f08b",
        "ed21086ff6682ab8495ecbfbb697af4a",
        "5a2585ff3524f319dfd1f6b735c9a18d",
        "0e61444507f0a780a1c83b612eb5fb9b",
        "b105aa5c696648c0f7aae9e3933f8fe0",
        "fec8f729e9e1d02248b949ce17674e0c",
        "d3323d5560d15d4bc03575dcd0f53ae9",
        "15fbf9d24dd05d9d64a18a8fd28f4dcc",
        "ac0f3bda53081eee547882b2cdc8b04f",
        "5dd3fadcd4ea6b922e1462431966c2bf",
        "4acb71816dad0ce9a53d8fee301d857c",
        "4c7e173f3a046919587db5b2640896e7",
        "8407dc0459d0b367eaced7e5dfdef8ed",
        "17e02409659223ff4e32cabd9ad352d9",
        "c49edc07086b27769eddb981359f56b2",
        "344822f5d8d53fe9aa7a1c7328cd2c59",
        "92259343c65ac0feab5cb56b2e851783",
        "e1e537b0bd37091c0ba4d5f614af9160",
        "dff1116c175ddaaa20f3985a3d88abc6",
        "3b1131a7c7273aa61cbd71b044e9beca",
        "431aab37ef168c383f078b9244008cee",
        "96c3bb8355d7e3ed7265095374f1c090",
        "c3a7d304cdb307f073bef5003d1b8b78",
        "627d884fc905cc353d0028076e39846b",
        "36ce0d88a6bb2d10e0dc0a697f64df4e",
        "dc8dbd035d42a5d8170976d5f532dab0",
        "01c2665e7ea15bc56cca6d955c2e8ae1",
        "c54ae7eeedc87ac52249684f012d3805",
        "2df9b3b8f21a682b20d9d77669087a7a",
        "fded473150a783586c12692fd57d0825",
        "580499e69f42c0ccba0d1f87a83e41e9",
        "99433cb83f1cd7176b7cdeaa7be49cd8",
        "fbd76e8265547376905b3b6004150064",
        "362768496052ae0dfbe909a9b5c6f54e",
        "4f33581089c90944e5ad950646b17712",
        "bffe93cdfe4b8833190e0a59c779e027",
        "78e042b792c3af7faf7a6ebfedf6af9e",
        "51a59c881726c2887efe9752bd9db715",
        "a46ecf03d3f4038ba3de4ae4ac28170f",
        "48d025f7cc34ac29c21d03b2c1f36449",
        "8c9ceb77d61c20cb96ee652eb7b838c9",
        "47a5882c89671429ae532339b7f333ce",
        "a0b735557416ff3d08d3d8440393061a",
        "976d3b3a8fbdf33d525075a9288455ab",
        "636ca4c1db1c4450431ecd7e10a5e671",
        "8c5cd12180027ee6535a837bd4f0259a",
        "b82315333974c76793b3c7f517fe977c",
        "6143d1f3472cd7cf08e3780918019158",
        "20d032426fd66d49bec4f99579252cfa",
        "398ee715d1dfd058a912bc7768d35f82",
        "1f678678966444fb53d118b8134ceb94",
        "d6641f3ed9444eae2b77ba68d3552f6a",
        "ab2babaa19539895a5285c1ded6de8c6",
        "5bc61d3cd53582b859db9cf04fc7e250",
        "5deb619ed27c2754df4f9c7e3ce16b82",
        "b81a322830fee59c75985626f7e0a8b5",
        "e2313ad53d58e181c5fbaef29e5772c3",
        "70d2aa99ef48b6cf1c0e8c107c0e121d",
        "0633cdb06253a2b11e9a9ca234a3e9c3",
        "bd1cbb9764fba94e8f1c0d1c024487af",
        "301cbdbf26210596f9b22123abff0ca8",
        "1fc2448ee192a1d0806ae1eb6fcc81fe",
        "306247030d0b6442c3ded42e9ca99872",
        "1c8f9a0786a01db1d06989345887967e",
        "256ec3a54aaae719aae88d8f9c7f9b5f",
        "45645896cccec48191916fec482979d9",
        "c3a19c728d6fd39925bd63abe15aa446",
        "15f45c4cd8fd4a6c0a3fae14ccafff47",
        "a082c46b09772739af41f01676e1d0d1",
        "14928418f94f5d35b182001ae0160455",
        "dfbc5bc946c72650adaaf570f11a1e80",
        "8a312e3e30d2e8fd1cf8873c3abe1d8c",
        "ef425403acaabfb2a5b3f6ab0aafce8c",
        "c78d471822dd961a53afe23e6c2dfa61",
        "a40f670d8de3784b54784daf63095d88",
        "49a72ace7fd54d8d0833bb2590db58aa",
        "38e3808d28de73af3578f6d64020e1fc",
        "a8be6ab39263d2edf61acafc60949921",
        "d9c16bf0032800916e948ea26624a253",
        "dbf3a62ff403c3ba94d5ab1e6219f5bc",
        "3a6415de684e2978ce17543d66d523f6",
        "2f69a681ee1ff927df1bdbd5431ced1d",
        "e55c0390872735ec285dad8ebdd939e0",
    ]
    start_beans = 0
    end_beans = 0
    URL = "https://www.duokan.com"

    def __init__(self, cookies: str):
        self.session = requests.Session()
        self.device_id = re.search(r"device_id=(.*?);", cookies).groups()[0]
        self.headers = {
            "Accept-Encoding": "gzip, deflate",
            "Cookie": cookies,
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1; MX5 Build/LMY47I)",
        }

    def get_csrf_params(self):
        time_sec = int(time.time())
        list_of_str = list(self.device_id + "&" + str(time_sec))
        i = 0
        csrf_code = 0
        while i < len(list_of_str):
            csrf_code = (csrf_code * 131 + ord(list_of_str[i])) % 65536
            i += 1
        param = {"_t": time_sec, "_c": csrf_code}
        return param

    def template(self, func_url: str, param: dict = {}):
        param.update(self.get_csrf_params())
        r = self.session.post(
            self.URL + func_url,
            data=param,
            headers=self.headers,
        ).json()
        return r

    def check_in(self):
        """
        每日签到
        """
        r = self.template("/checkin/v0/checkin")
        return f"【每日签到】{r['msg']}"

    def get_free_book(self):
        """
        获取限免书籍
        """
        r = self.template("/hs/v4/channel/query/2027")
        bookid = r["items"][0]["data"]["book_id"]
        param = {
            "payment_name": "BC",
            "ch": "VSZUVB",
            "book_id": bookid,
            "price": 0,
            "allow_discount": 1,
        }
        r = self.template("/store/v0/payment/book/create", param)
        return f"【今日限免】{r['book']['title']}(作者：{r['book']['authors']}) [{r['msg']}]"

    def delay_beans(self, expire):
        """
        书豆延期
        """
        param = {"date": expire, "withid": 1}
        r = self.template("/store/v0/award/coin/delay", param)
        return r["msg"]

    def get_info(self, flag="start"):
        """
        查询账号书豆
        """
        param = {"sandbox": 0, "withid": 1}
        r = self.template("/store/v0/award/coin/list", param)["data"]["award"]
        coins = []
        info = ""
        for i in r:
            coins.append(i["coin"])
            if flag == "start":
                self.start_beans = sum(coins)
            elif flag == "end":
                self.end_beans = sum(coins)
                info += f"\n            - {i['coin']} 书豆(有效期 {i['expire']})"
                if i["delay"] == 1:
                    info += f"[延期{self.delay_beans(i['expire'])}]"
        if flag == "end":
            return f"【书豆统计】共获得{self.end_beans - self.start_beans} 书豆（运行前{self.start_beans} 书豆,运行后{self.end_beans} 书豆）\n{info}"

    def tiyan(self, signcode):
        param = {"code": "KYKJF7LL0G", "chances": 1, "sign": signcode, "withid": 1}
        r = self.template("/events/common_task_gift", param)["msg"]
        return r

    def getchances(self):
        """
        获取体验次数
        """
        tiyan_beans = 0
        param = {"code": "KYKJF7LL0G", "withid": 1}
        r = self.template("/events/common_task_gift_check", param)["chances"]
        if r == 0:
            return "【体验书豆】今日体验任务已全部完成"
        else:
            for signcode in self.signcodes:
                msg = self.tiyan(signcode)
                if msg == "成功":
                    tiyan_beans += 1
            return f"【体验书豆】共获得{tiyan_beans * 30} 书豆"

    def daily(self):
        """
        日常任务
        """
        daily_codes = [
            "K7S36GFSZC",
            "A2AMBFHP6C",
            "K5HHKUU14D",
            "J18UK6YYAY",
            "1BJGW140U5",
        ]
        for code in daily_codes:
            flag = 0
            while flag == 0:
                time.sleep(0.5)
                param = {"code": code, "chances": 3, "withid": 1}
                r = self.template("/events/tasks_gift", param)
                flag = r["result"]
        return f"【日常任务】已完成"

    def download(self):
        """
        下载任务
        """
        beans = 0
        flag = 0
        while flag == 0:
            param = {"code": "J18UK6YYAY", "chances": 17, "withid": 1}
            r = self.template("/events/common_task_gift", param)
            flag = r["result"]
            if r["msg"] == "成功":
                beans += 1
        return f"【下载任务】获得{beans * 30} 书豆"

    def drawingadd(self):
        """
        增加大转盘次数
        """
        for i in range(6):
            param = {"code": "8ulcky4bknbe_f", "count": 1, "withid": 1}
            r = self.template("/store/v0/event/chances/add", param)

    def drawing(self):
        """
        大转盘抽奖
        """
        flag = 0
        while flag == 0:
            param = {"code": "8ulcky4bknbe_f", "withid": 1}
            r = self.template("/store/v0/event/drawing", param)
            flag = r["result"]
        return f"【转盘抽奖】已完成"

    def push(self, content):
        tg_bot_token = os.environ["TG_BOT_TOKEN"]
        tg_user_id = os.environ["TG_USER_ID"]
        send_data = {
            "chat_id": tg_user_id,
            "text": "📣多看阅读签到通知📣" + "\n\n" + content,
            "disable_web_page_preview": "true",
        }
        response = requests.post(
            url=f"https://api.telegram.org/bot{tg_bot_token}/sendMessage",
            data=send_data,
        )
        print(response.json()["ok"])


if __name__ == "__main__":
    cookies = os.environ["COOKIES"].split("\n")
    start_time = time.time()
    for index, cookie in enumerate(cookies):
        print(f"\n=====开始第 {index+1} 个多看账号=====")
        tz = ""
        dksign = DuoKan(cookie)
        dksign.get_info()
        tz += dksign.check_in() + "\n"
        tz += dksign.get_free_book() + "\n"
        tz += dksign.getchances() + "\n"
        tz += dksign.daily() + "\n"
        tz += dksign.download() + "\n"
        dksign.drawingadd()
        tz += dksign.drawing() + "\n"
        tz += dksign.get_info("end")
        print(tz)
        dksign.push(tz)
    print(f"\n\n🕛耗时：{(time.time() - start_time):.2f} 秒")
