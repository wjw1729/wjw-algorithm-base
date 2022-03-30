# codeforces-go

## 算法 Algorithm

由于算法知识点繁杂，将自己学习到的算法、做过的题目分类整理好是有必要的。

一个算法模板应当涵盖以下几点：
- 对该算法的基本介绍（核心思想、复杂度等）
- 参考链接或书籍章节（讲的比较好的资料）
- 模板代码（可以包含一些注释、使用说明）
- 模板补充内容（常见题型中的额外代码、建模技巧等）
- 相关题目链接（模板题、经典题、思维转换题等）


## 算法目录

- 数据结构
  - 单调栈 monotone_stack.py
  - 单调队列 monotone_queue.py
    - 二维单调队列
  - 双端队列 deque.py
  - 堆（优先队列）heap.py
    - 支持修改、删除指定元素
  - [并查集 union_find.py](/copypasta/union_find.go)
    - 点权
    - 边权（种类）
    - 持久化
    - 回滚操作（动态图连通性）
  - [稀疏表（ST 表）sparse_table.py](/copypasta/sparse_table.go)
  - [树状数组 fenwick_tree.py](/copypasta/fenwick_tree.go)
  - [线段树 segment_tree.py](/copypasta/segment_tree.go)
    - 延迟标记（懒标记）
    - 动态开点
    - 线段树合并
    - 线段树分裂
    - 持久化（主席树）
  - [左偏树（可并堆）leftist_tree.py](/copypasta/leftist_tree.go)
  - [笛卡尔树 cartesian_tree.py](/copypasta/cartesian_tree.go)
  - [二叉搜索树公共方法 bst.py](/copypasta/bst.go)
  - [Treap treap.py](/copypasta/treap.go)
  - [伸展树 splay.py](/copypasta/splay.go)
  - [动态树 LCT link_cut_tree.py](/copypasta/link_cut_tree.go)
  - [红黑树 red_black_tree.py](/copypasta/red_black_tree.go)
  - [替罪羊树 scapegoat_tree.py](/copypasta/scapegoat_tree.go)
  - [k-d 树 kd_tree.py](/copypasta/kd_tree.go)
  - 珂朵莉树（ODT）
    - [数组版 odt.py](/copypasta/odt.go)
    - [平衡树版 odt_bst.py](/copypasta/odt_bst.go)
  - [根号算法（分块）sqrt_decomposition.py](/copypasta/sqrt_decomposition.go)
  - [莫队算法 mo.py](/copypasta/mo.go)
     - 普通莫队
     - 带修莫队
     - 回滚莫队
     - 树上莫队
- [字符串 strings.py](/copypasta/strings.go)
  - 字符串哈希
  - KMP
    - 最小循环节
  - 扩展 KMP（Z algorithm）
  - 最小表示法
  - 最长回文子串 
    - Manacher 算法
  - 后缀数组（SA）
  - [字典树 trie.py](/copypasta/trie.go)
    - 持久化
    - AC 自动机
  - [异或字典树 trie01.py](/copypasta/trie01.go)
    - 持久化
    - Hack：构造一组数据，最大化树上的节点数
- 数学
  - [数论 math.py](/copypasta/math.go)
    - 最大公因数（GCD）
    - 类欧几里得算法 ∑⌊(ai+b)/m⌋
    - Pollard-Rho 质因数分解算法
    - 埃氏筛
    - 线性筛
    - 欧拉函数
    - 原根
    - 扩展 GCD
      - 二元一次不定方程
    - 逆元
      - 线性求逆元
    - 中国剩余定理（CRT）
      - 扩展中国剩余定理
    - 离散对数
      - 大步小步算法（BSGS）
        - 扩展大步小步算法
      - 二次剩余
      - Jacobi 符号
    - 组合数学
      - 卢卡斯定理
      - 卡特兰数
      - 默慈金数
      - 那罗延数
      - 斯特林数
        - 第一类斯特林数（轮换）
        - 第二类斯特林数（子集）
      - 贝尔数
    - 莫比乌斯函数
    - 数论分块
    - 杜教筛
    - 容斥原理
  - [快速傅里叶变换 FFT math_fft.py](/copypasta/math_fft.go)
  - [快速数论变换 NTT math_ntt.py](/copypasta/math_ntt.go)
    - 包含多项式全家桶（求逆、开方等等）
  - [快速沃尔什变换 FWT math_fwt.py](/copypasta/math_fwt.go)
  - [连分数、佩尔方程 math_continued_fraction.py](/copypasta/math_continued_fraction.go)
  - [线性代数 math_matrix.py](/copypasta/math_matrix.go)
    - 矩阵相关运算
    - 高斯消元
    - 行列式
    - 线性基
  - [数值分析 math_numerical_analysis.py](copypasta/math_numerical_analysis.go)
    - 自适应辛普森积分
    - 拉格朗日插值
  - [计算几何 geometry.py](/copypasta/geometry.go)
    - 线与点
    - 线与线
    - 圆与点
      - 最小圆覆盖
        - 随机增量法
      - 固定半径覆盖最多点
    - 圆与线
    - 圆与圆
    - 圆与矩形
    - 最近点对
    - 多边形与点
    - 凸包
    - 最远点对
      - 旋转卡壳
    - 半平面交
  - [博弈论 games.py](/copypasta/games.go)
    - SG 函数
- [动态规划 dp.py](/copypasta/dp.go)
  - 背包
    - 0-1 背包
    - 完全背包
    - 多重背包
    - 分组背包
    - 树上背包（依赖背包）
    - 字典序最小方案
  - 线性 DP
    - 最大子段和
    - LCS
    - LPS
    - LIS
      - 狄尔沃斯定理
    - LCIS
    - 长度为 m 的 LIS 个数
    - 本质不同子序列个数
  - 区间 DP
  - 环形 DP
  - 状压 DP
    - 旅行商问题（TSP）
    - 高维前缀和（SOS DP）
    - 插头 DP
  - 数位 DP
  - 倍增优化 DP
  - 斜率优化 DP（CHT）
  - 树形 DP
    - 树的直径个数
    - 在任一直径上的节点个数
    - 树上最大独立集
    - 树上最小顶点覆盖
    - 树上最小支配集
    - 树上最大匹配
    - 换根 DP（二次扫描法）
- [图论 graph.py](/copypasta/graph.go)
  - 链式前向星
  - 欧拉回路和欧拉路径
    - 无向图
    - 有向图
  - 割点
  - 割边（桥）
  - 双连通分量（BCC）
    - v-BCC
    - e-BCC
  - 最短路
    - Dijkstra
    - SPFA（队列优化的 Bellman-Ford）
      - 差分约束系统
    - Floyd-Warshall
    - Johnson
    - 0-1 BFS（双端队列 BFS）
    - 字典序最小最短路
  - 最小环
  - 最小生成树（MST）
    - Kruskal
    - Prim
  - 单度限制最小生成树
  - 次小生成树
  - 曼哈顿距离最小生成树
  - 最小差值生成树
  - 最小树形图
    - 朱刘算法
  - 二分图判定（染色）
  - 二分图找奇环
  - 二分图最大匹配
    - 匈牙利算法
  - 带权二分图最大完美匹配
    - Kuhn–Munkres 算法
  - 拓扑排序
  - 强连通分量（SCC）
    - Kosaraju
    - Tarjan
  - 2-SAT
  - 基环树
  - 最大流
    - Dinic
    - ISAP
    - HLPP
  - 最小费用最大流
    - SPFA
    - Dijkstra
  - 三元环计数
  - 四元环计数
  - 仙人掌
  - [树上问题 graph_tree.py](/copypasta/graph_tree.go)
    - 直径
    - 重心
      - 点分治
    - 最近公共祖先（LCA）
      - 倍增
      - ST 表
      - Tarjan
      - 树上差分
    - 树链剖分（重链剖分，HLD）
    - 长链剖分
    - 树上启发式合并（DSU）
    - 树分块
    - Prufer 序列
- 其他
  - [位运算笔记 bits.py](/copypasta/bits.go)
    - bitset
    - 区间位运算 trick（含 GCD）
  - [二分 三分 sort.py](/copypasta/sort.go)
    - 0-1 分数规划
    - 整体二分
  - [搜索 search.py](/copypasta/search.go)
    - 枚举排列
    - 枚举组合
    - 生成下一个排列
    - 康托展开
    - 逆康托展开
    - 折半枚举
      - 超大背包问题
    - 枚举子集
      - Gosper’s Hack
  - [随机算法 rand.py](/copypasta/rand.go)
    - 模拟退火
  - [杂项A common.py](/copypasta/common.go)
    - 算法思路整理
    - 前缀和
    - 二维前缀和
    - 二维差分
    - 离散化
  - [杂项B misc.py](/copypasta/misc.go)
- [快读模板 io.py](/copypasta/io.go)


## 如何选择题目 How to Choose Problems

### Rating < 2100

这一阶段主要目标是提高对问题的观察能力。做构造题可以针对性地训练这一点。

选择难度在自己 rating 到 rating+200 范围内的构造题 (tag: constructive algorithms)，按照过题人数降序做题，比如 [1700,1900] 区间的就是下面这个链接：

[https://codeforces.com/problemset?order=BY_SOLVED_DESC&tags=constructive+algorithms%2C1700-1900](https://codeforces.com/problemset?order=BY_SOLVED_DESC&tags=constructive+algorithms%2C1700-1900)

通过大量的构造题训练，提高观察能力，快速找到切题入口。

### Rating >= 2100

这一阶段要想上分，应以 DP 为主，图论和数据结构为辅。难度范围选择同上，可以根据自己在该项的能力上下调整。

我的 Codeforces 账号：

[![0x3F](https://img.shields.io/badge/0x3F-MASTER%202189-orange?style=for-the-badge)](https://codeforces.com/profile/0x3F)


## 测试及对拍 Testing

编写一个 `run(io.Reader, io.Writer)` 函数来处理输入输出。这样写的理由是：

- 在 `main` 中调用 `run(os.Stdin, os.Stdout)` 来执行代码；
- 测试时，将测试数据转换成 `strings.Reader` 当作输入，并用一个 `strings.Builder` 来接收输出，将这二者传入 `run` 中，然后就能比较输出与答案了；
- 对拍时需要实现一个暴力算法 `runAC`，参数和 `run` 一样。通过[随机数据生成器](/main/testutil/rand.go)来生成数据，分别传入 `runAC` 和 `run`，通过比对各自的输出，来检查 `run` 中的问题。

具体可以见 Codeforces 代码仓库 [main](/main)，所有非交互题的代码及其对应测试全部按照上述框架实现。

例如：[1439C_test.go](/main/1400-1499/1439C_test.go)

交互题的写法要复杂一些，需要把涉及输入输出的地方抽象成接口，详见 [interactive_problem](/copypasta/template/interactive_problem)。

## 学习资料及题目 Resources

注：由于入门经典上选了很多区域赛的题，一部分题目可以在 GYM 上找到，这样可以就可以用 Go 编程提交了。

[算法竞赛入门经典（第二版）](https://github.com/aoapc-book/aoapc-bac2nd)

[算法竞赛入门经典训练指南](https://github.com/klb3713/aoapc-book/tree/master/TrainingGuide/bookcodes)

[算法竞赛入门经典训练指南（升级版）](https://gitee.com/sukhoeing/aoapc-training-guide2)

[算法竞赛进阶指南](https://github.com/lydrainbowcat/tedukuri)

[算法竞赛入门到进阶](https://github.com/luoyongjun999/code)

[OI Public Library（含国家队论文）](https://github.com/enkerewpo/OI-Public-Library)

[算法竞赛 (ICPC, OI, etc) 论文，课件，文档，笔记等](https://github.com/LzyRapx/Competitive-Programming-Docs)

[算法竞赛课件分享 by hzwer](https://github.com/hzwer/shareOI)

[算法第四版 Java 源码](https://algs4.cs.princeton.edu/code/)

[数据结构和算法动态可视化](https://visualgo.net/zh)

[OI Wiki](https://oi-wiki.org/)

[CP-Algorithms](https://cp-algorithms.com/)

[洛谷日报](https://www.craft.do/s/N0l80k2gv46Psq)

[All the good tutorials found for Competitive Programming](https://codeforces.com/blog/entry/57282)

[Codeforces Problem Topics](https://codeforces.com/blog/entry/55274)

[GeeksforGeeks 上的算法合集](https://www.geeksforgeeks.org/how-to-prepare-for-acm-icpc/)

[Pepcy 模板](http://pepcy.cf/icpc-templates/)

[F0RE1GNERS 模板](https://github.com/F0RE1GNERS/template)

[【模板整合计划】目录](https://www.cnblogs.com/Xing-Ling/p/10930556.html)

[算法学习笔记（目录）](https://zhuanlan.zhihu.com/p/105467597)

[洛谷模板题（建议按难度筛选）](https://www.luogu.com.cn/problem/list?keyword=%E6%A8%A1%E6%9D%BF&page=1)

[能力全面提升综合题单](https://www.luogu.com.cn/training/9391)

[Luogu Problem List](https://github.com/SFOI-Team/luogu-problem-list/blob/master/list.md)

[洛谷原试炼场](https://www.luogu.com.cn/paste/0id3h6on)

[Links of ICPC/CCPC Contests from China](https://codeforces.com/blog/entry/84429)

### AtCoder 版《挑战程序设计竞赛》

[AtCoder 版！蟻本 (初級編)](https://qiita.com/drken/items/e77685614f3c6bf86f44)

[AtCoder 版！蟻本 (中級編)](https://qiita.com/drken/items/2f56925972c1d34e05d8)

[AtCoder 版！蟻本 (上級編)](https://qiita.com/drken/items/9b311d553aa434bb26e4)

[AtCoder 版！蟻本 (発展的トピック編)](https://qiita.com/drken/items/0de3d205690d92307b7c)

### 待整理

[【杂文】记一些有用的神奇网站](https://www.cnblogs.com/Xing-Ling/p/10897760.html)

[偶然在 GitHub 上发现的超长列表](https://github.com/dhs347/Dream/blob/master/%E8%AE%A1%E5%88%92/%E8%AE%A1%E5%88%92%E4%B9%A6/A%E8%AE%A1%E5%88%92_%E9%98%B6%E6%AE%B51.md)

[算法竞赛训练中较难的部分](https://blog.csdn.net/skywalkert/article/details/48924861)

[算法竞赛中可能不太会遇到的论文题](https://blog.csdn.net/skywalkert/article/details/48878925)

[[杂谈]OI/ACM中冷门算法](https://zhuanlan.zhihu.com/p/21924647)

https://blog.csdn.net/calabash_boy/article/details/79973483

https://github.com/zimpha/algorithmic-library

https://www.luogu.com.cn/blog/command-block/blog-suo-yin-zhi-ding-post

https://wcysai.github.io/

https://www.luogu.com.cn/blog/Troverld/index

## 其他 Others

My GoLand `Live Templates` and `Postfix Completion` [settings](/misc/my_goland_template)

### Useful Tools

[Draw Geometry](https://csacademy.com/app/geometry_widget/)

[Draw Graph](https://csacademy.com/app/graph_editor/)

[OEIS](https://oeis.org/)

[Wolfram|Alpha](https://www.wolframalpha.com/)

[UpSolve.me](https://upsolve.me/)

[Codeforces Upsolving Helper](https://codeforces-upsolving-helper.herokuapp.com/)

[Contests Filter](https://codeforceshelper.herokuapp.com/contests)

[Codeforced](http://codeforced.github.io/handle/)

[Codeforces Visualizer](https://cfviz.netlify.app/)

[Codeforces Solve Tracker](https://tom0727.gitee.io/cf-problems/)

[Another Codeforces Solve Tracker](https://cftracker.netlify.app/contests)

### Rating and Difficulties

[Open Codeforces Rating System](https://codeforces.com/blog/entry/20762)

[How to Interpret Contest Ratings](https://codeforces.com/blog/entry/68288)

[Codeforces: Problem Difficulties](https://codeforces.com/blog/entry/62865)

[Elo rating system](https://en.wikipedia.org/wiki/Elo_rating_system#Theory)

### Stay Healthy

[Exercises!](https://musclewiki.org/)
