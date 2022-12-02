# 如何在你的unity项目中接入pocoSDK

## 为什么要接入Poco-SDK
先来聊一聊我们为什么要接入Poco-SDK。目前我们的Poco框架支持Android和iOS的原生应用，
并且无需嵌入任何代码，只要在IDE中连接了Android或是iOS设备，然后直接在poco辅助窗选
择对应的Android或者是iOS模式， 除了支持原生APP之外，Poco框架还支持大部分主流游戏引
擎开发的游戏应用，但是与原生应用不一样，poco获取游戏项目的UI树，需要事先在游戏项目源
码中，接入Poco-SDK，开启1个poco服务，这样我们在启动游戏项目的时候，才能够获取到游戏
应用的控件信息，并利用这些控件进行自动化测试工作。
所以有使用Poco框架测试游戏应用需求的同学，可以先跟开发了解下自己的游戏项目是什么引擎的，
然后再在我们官网上找到对应的poco-sdk接入到项目中，最后打包出来测试。

### 目前我们提供了下述引擎的poco-SDK和接入教程：

1. unity3d接入教程 ：https://poco-chinese.readthedocs.io/zh_CN/latest/source/doc/integration.html#unity3d
2. cocos2dx-lua接入教程：https://poco-chinese.readthedocs.io/zh_CN/latest/source/doc/integration.html#cocos2dx-lua
3. cocos2dx-js接入教程：https://poco-chinese.readthedocs.io/zh_CN/latest/source/doc/integration.html#cocos2dx-js-beta
4. cocos-creator接入教程：https://poco-chinese.readthedocs.io/zh_CN/latest/source/doc/integration.html#cocos-creator
5. Egret接入教程：https://github.com/AirtestProject/Poco-SDK/tree/master/Egret
6. UE4接入教程：https://mp.weixin.qq.com/s?__biz=MzUxMDc4NTkwMA==&mid=2247484258&idx=1&sn=0fec4461bc870077af4e096b4
   94d646a&chksm=f97ce361ce0b6a77c885193a900d2be08d22c3cf86a0e90a5fb0e83758aaffc65a9d00ec3927&token=1860040772&
   lang=zh_CN#rd
7. 自行接入其它引擎的教程：https://poco-chinese.readthedocs.io/zh_CN/latest/source/doc/implementation_guide.html
8. WebView检视：https://airtest.doc.io.netease.com/IDEdocs/poco_framework/poco_webview/
9.无需接入pocoSDK的平台：Android原生、iOS原生
10.暂不支持的平台：Windows、MacOS等

### 在unity项目接入Poco-SDK
了解完Poco框架目前支持哪些类型的应用，并且知道哪些应用需要接入poco-SDK之后，我们来具体实操一下，以unity项目为例，
如何接入poco-SDK，然后在IDE中检索unity项目的控件：
1. unity项目接入poco-SDK的步骤
1）下载Poco-SDK包
这个直接到我们的GitHub上面clone下来即可：https://github.com/AirtestProject/Poco-SDK 。

2）把Unity3D文件夹放到项目脚本中

把刚才clone下来的压缩包 Poco-SDK-master.zip 解压，然后将其中的Unity3D文件夹放到你Unity项目的Scripts的任意位置中：

注意：注意，这里所说的Scripts指的就是unity游戏项目的源码。

3）根据UI类型选择

询问程序使用的是哪种UI方式，SDK中有三个文件夹 ugui 、 ngui 、 fairygui ，保留其中一种删除另外两种，比如上图选择的就是 ugui 。其余两种请务必删除，不然unity会报错。


4）在unity载入脚本

创建一个空的 GameObject (右键-Create Empty)，添加脚本(Add Component)：


其他参数默认即可，GameObject 名字随意。或者，同学们也可以在 root 或者 主camera 这些 GameObject 上添加脚本（Add Component） Unity3D/PocoManager.cs 。

有同学可能会问，为什么要新建空的 GameObject 或者是选择 root 、 主camera 这些 GameObject来添加脚本呢？其实这都是为了将脚本挂载到1个 不会在游戏的生命周期中被销毁的节点 上去，并且在游戏开始时，尽快开启poco服务。

2. IDE连接game窗口查看控件树

在unity编辑器中，单独拖出来game窗口，然后IDE连接上这个game窗口，选择unity模式，可以查看该项目的poco控件树：


3. 打包成Android包在IDE进行测试

1）文件-BuildSettings-平台选择Android-切换平台


2）成功切换成Android平台之后，打开玩家设置


3）选择Player，设置包名


4）设置完成后，点击生成，等待打包完成


打包成功之后，在待测设备安装上，然后打开unity项目，在poco辅助窗选择unity模式，可以查看、检索控件树。


之后，我们就可以在这个测试包上编写Poco自动化脚本了。

接入Poco-SDK的常见问题
了解完如何在项目中接入Poco-SDK并打出Android测试包之后，接下来我们来看下接入Poco-SDK的常见问题：

1. 如何知道自己的项目是否需要接入Poco-SDK？

就像我们刚才所说的那样，除了Android和iOS的原生应用，其余由各种引擎开发的游戏项目，是需要提前接入Poco-SDK，才能够使用我们的poco框架来进行自动化测试的。

2. 接入Poco-SDK的前提条件是什么？

需要有该游戏的项目源码。非公司内部的游戏我们是不能获取源码并接入sdk的哈。另外我们要询问公司的开发人员，目前需要测试的这款游戏是由什么引擎开发的；然后到我们Airtest官方文档上查询这个引擎游戏的poco-SDK教程，根据教程步骤完成接入工作，再来查看游戏项目的UI树。如条件允许，可以让开发帮忙接入并且打包之后给我们测试。

3. 为什么选择根节点或者主camera来添加脚本？

其实这都是为了将脚本挂载到1个 不会在游戏的生命周期中被销毁的节点 上去，并且在游戏开始时，尽快开启poco服务。这样游戏切换任意场景时，此节点都会常驻，并且永不销毁。能保证poco服务也能在启动游戏之后一直开启着。

4. 自研引擎可不可以接入poco-SDK?

自研引擎也可以自行接入Poco-SDK，可以参考我们的官方文档：https://poco.readthedocs.io/zh_CN/latest/source/doc/implementation_guide.html
