# SimpleDBmanageSystem
一个简单的用来给execl表格上数据的python项目

rule NO1,本程序基于chatgpt开发，不要商用，没有版权

rule NO2,不要随意传播，这也算我的辛苦努力的内容，不要乱搞

rule NO3,这个类似于database的系统，并不是db，不要弄混，我觉得sql语句太不像给人写的了，但是我也没啥好办法，这个玩意可能会有future update，但是有future update有点不太可能，如果有想跟我一起开发的发到issue里面或者想办法私信我，咱们可以讨论，记得附一份简历如果我不认识你的话

rule NO4,暂时没想好，反正这里应该有一个rule，anyway，如果要使用本项目请一定遵守以上全部rule，违反者自负责任


readme

use case

``create_table 招聘信息 公司 岗位 投递时间 收到email时间 是否有面试 收到结果的时间 招多少人 地点 分类``
创建table并且创建列（注意一定要一起创建）

``select_table 招聘信息``
选择table，如果有()那么一定是英文括号

``input 公司A 前端开发 20230310 20230315 是 20230320 2 上海 国企``
input数据，注意不能用-，日期要连起来，不然输入会崩

``view_table_head``
查看表头，避免你input的时候填错了

``output_table``
备用方案，假设没输出表用这个强制输出

``view_column 岗位``
查看某一个列独特的项有什么，输出这些项，防止你写到一半忘了tag是啥
