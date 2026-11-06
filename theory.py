Experiment 1 – RPC and RMI
Concept	Viva-ready definition
Distributed Computing	A computing model in which multiple computers work together to complete a common task.
Client	A program or machine that requests a service from another machine.
Server	A program or machine that receives requests and provides services.
RPC	Remote Procedure Call allows a program to execute a function on another computer as if it were a local function.
RMI	Remote Method Invocation allows an object to invoke methods of an object located in another JVM.
Stub	A proxy that represents a remote procedure or object and handles communication between client and server.
Marshalling	Converting parameters into a format suitable for network transmission.
Unmarshalling	Converting received data back into its original format.
Remote Object	An object whose methods can be accessed from another machine or JVM.
Client-Server Architecture	An architecture in which clients request services and servers process those requests.
Middleware	Software that acts as an intermediate layer between applications and the underlying system.

Experiment 2 – Multithreading
Concept	Viva-ready definition
Process	A program that is currently being executed.
Thread	The smallest unit of execution within a process.
Multithreading	Executing multiple threads within a single process concurrently.
Concurrency	Multiple tasks making progress during overlapping periods of time.
Parallelism	Executing multiple tasks simultaneously using multiple processing units.
Synchronization	Coordinating multiple threads to ensure correct access to shared resources.
Race Condition	A situation where the result depends on the order or timing of concurrent execution.
Critical Section	A section of code where shared resources are accessed or modified.
Mutex	A locking mechanism that allows only one thread to access a protected resource at a time.
Lock	A mechanism used to restrict access to shared resources.
Deadlock	A situation where two or more processes wait indefinitely for resources held by one another.
Starvation	A situation where a process waits indefinitely because other processes keep receiving resources.
Thread Safety	The ability of a program to work correctly when accessed by multiple threads simultaneously.
Thread Pool	A collection of reusable threads used to execute multiple tasks efficiently.
Join	An operation that makes one thread wait until another thread finishes execution.

Experiment 3 – Clock Synchronization
Concept	Viva-ready definition
Clock Synchronization	The process of making different computers' clocks agree with each other.
Physical Clock	A clock that represents actual real-world time.
Logical Clock	A mechanism that assigns timestamps to events to determine their ordering.
Clock Drift	The difference in the rate at which a clock progresses compared to a reference clock.
Clock Skew	The difference between the time readings of two clocks at a particular instant.
Cristian's Algorithm	A clock synchronization algorithm in which a client adjusts its clock using time received from a time server.
Berkeley Algorithm	A synchronization algorithm in which a master calculates the average time of participating computers and sends clock adjustments.
Lamport Clock	A logical clock that uses a single counter to establish the ordering of events.
Vector Clock	A logical clock that uses an array of counters to track causal relationships between events.
NTP	Network Time Protocol is used to synchronize computer clocks over a network.
Happened-Before	A relation that determines whether one event causally occurred before another event.
Concurrent Events	Events that have no causal relationship with each other.
Timestamp	A value assigned to an event to indicate its time or logical ordering.
Causality	The relationship between events where one event influences or causes another.

Important formulas
Lamport clock on receiving a message:
\[
C=\max(C,T)+1
\]

Cristian's estimated server time:
\[
T_s+\frac{RTT}{2}
\]

Experiment 4 – Election Algorithms
Concept	Viva-ready definition
Election Algorithm	An algorithm used to select a coordinator among multiple processes in a distributed system.
Coordinator	A process responsible for managing and coordinating activities in a distributed system.
Leader Election	The process of selecting one process as the leader of a distributed system.
Bully Algorithm	An election algorithm in which the active process with the highest ID becomes the coordinator.
Ring Algorithm	An election algorithm in which an election message circulates through a logical ring to select a coordinator.
Election Message	A message sent by a process to initiate or participate in an election.
Coordinator Message	A message announcing the newly elected coordinator to other processes.
Process ID	A unique identifier assigned to each process in a distributed system.
Active Process	A process that is currently operational and participating in the system.
Failure Detection	The process of identifying whether a node or process has stopped functioning.
Logical Ring	A communication arrangement in which each process has a next process, forming a circular structure.

Experiment 5 – Data Consistency and Replication
Concept	Viva-ready definition
Data Replication	The process of maintaining multiple copies of the same data on different servers.
Replica	A copy of data maintained on another node or server.
Data Consistency	The property of ensuring that data remains correct and follows defined consistency rules across replicas.
Strong Consistency	A consistency guarantee where reads observe the latest successful write, according to the system's consistency model.
Eventual Consistency	A consistency model where all replicas eventually become identical if no new updates occur.
Synchronous Replication	Replication in which the system waits for required replica acknowledgements before confirming a write.
Asynchronous Replication	Replication in which the primary confirms a write without waiting for all replicas to update.
CAP Theorem	A theorem stating that during a network partition, a distributed system cannot guarantee both consistency and availability.
Network Partition	A situation where groups of computers cannot communicate due to network failure.
Quorum	The minimum number of replicas required to participate in an operation.
Sequential Consistency	A model in which operations appear to execute in one order while preserving each process's program order.
Conflict Resolution	The process of resolving different updates received by multiple replicas.
Read-Your-Writes	A consistency guarantee where a user can always see their own successful updates in subsequent reads.

Experiment 6 – Load Balancing
Concept	Viva-ready definition
Load Balancing	The process of distributing incoming workloads across multiple servers.
Load Balancer	A component that distributes requests among available backend servers.
Round Robin	A load balancing algorithm that distributes requests sequentially among servers.
Least Connections	An algorithm that assigns new requests to the server with the fewest active connections.
Weighted Round Robin	An algorithm that distributes requests according to the assigned weight of each server.
Workload	The amount of work or number of tasks assigned to a system.
Throughput	The number of requests processed per unit of time.
Response Time	The time taken by a system to respond to a request.
Horizontal Scaling	Increasing capacity by adding more machines or servers.
Vertical Scaling	Increasing capacity by upgrading the hardware resources of an existing machine.
Health Check	A mechanism used to verify whether a server is operational.
Server Overloading	A condition where a server receives more work than it can efficiently handle.
Fault Tolerance	The ability of a system to continue functioning despite component failures.

Experiment 7 – MapReduce, Hadoop and Spark
Concept	Viva-ready definition
Big Data	Extremely large and complex datasets that require specialized processing techniques.
MapReduce	A distributed programming model that processes large datasets using Map and Reduce operations.
Mapper	A component that processes input data and generates intermediate key-value pairs.
Reducer	A component that combines or aggregates values having the same key.
Shuffle and Sort	The process of grouping intermediate values with the same key and transferring them to reducers.
Hadoop	An open-source framework for distributed storage and processing of large datasets.
HDFS	Hadoop Distributed File System is used to store large files across multiple machines.
NameNode	The master component of HDFS that manages filesystem metadata.
DataNode	A component of HDFS that stores actual data blocks.
YARN	A Hadoop resource management and job scheduling framework.
Apache Spark	A distributed data-processing engine that supports fast, in-memory computation.
RDD	Resilient Distributed Dataset is an immutable collection of data distributed across multiple machines.
Cluster	A group of interconnected computers working together.
Data Locality	Processing data close to where it is stored to reduce network communication.
Lazy Evaluation	Delaying computation until an action requires the result.
Transformation	An operation that creates a new RDD or DataFrame from existing data.
Action	An operation that triggers computation and produces a result.

Experiment 8 – Fault Tolerance and Primary-Backup Replication
Concept	Viva-ready definition
Fault Tolerance	The ability of a system to continue operating even when some components fail.
Fault	A defect or abnormal condition that can cause incorrect system behaviour.
Failure	The inability of a system component to perform its intended function.
Primary-Backup Replication	A replication technique where one server acts as primary and others maintain backup copies.
Primary Server	The main server responsible for processing client requests and managing updates.
Backup Server	A secondary server that maintains replicated data and can take over if the primary fails.
Failover	Switching operations from a failed primary server to a backup server.
Failback	Returning operations to the original primary server after recovery.
Active-Active	A configuration where multiple servers actively process requests simultaneously.
Active-Passive	A configuration where one server is active and another remains on standby.
Heartbeat	A periodic message exchanged between nodes to indicate that they are operational.
Checkpointing	Saving the current system state periodically to support recovery after failure.
Split Brain	A condition where multiple nodes incorrectly believe they are the primary server.
Replication Lag	The delay between an update on the primary and its arrival at a replica.
Recovery	Restoring a failed system or component to a working state.

Experiment 9 – MPI Collective Communication
Concept	Viva-ready definition
MPI	Message Passing Interface is a standard used for communication between processes in parallel computing.
Parallel Computing	Solving a problem by dividing its work among multiple processing units.
Process	An independent execution unit participating in a parallel program.
Rank	A unique integer identifier assigned to each MPI process.
Communicator	A group of MPI processes that can communicate with each other.
MPI_COMM_WORLD	The default MPI communicator containing all processes started by the program.
Collective Communication	Communication operations in which all processes in a communicator participate.
Broadcast	An operation where one root process sends the same data to all other processes.
Scatter	An operation where the root process distributes different portions of data to other processes.
Gather	An operation that collects data from multiple processes at a root process.
Reduce	An operation that combines values from multiple processes and returns the result to the root.
Allreduce	An operation that combines values and makes the final result available to all processes.
Barrier	A synchronization operation where all processes must arrive before any can continue.
Point-to-Point Communication	Communication that takes place between two individual processes.
Root Process	The process responsible for distributing or collecting data in collective operations.

Experiment 10 – Parallel Matrix Multiplication
Concept	Viva-ready definition
Matrix	A rectangular arrangement of numbers in rows and columns.
Matrix Multiplication	A mathematical operation that multiplies rows of one matrix with columns of another matrix.
Parallel Matrix Multiplication	Dividing matrix multiplication work among multiple processors to reduce execution time.
Sequential Processing	Executing instructions one after another using a single processing flow.
Parallel Processing	Executing multiple parts of a task simultaneously.
Data Decomposition	Dividing input data into smaller parts for parallel processing.
Domain Decomposition	Dividing a computational problem into smaller subproblems assigned to different processes.
Master Process	The main process responsible for distributing work and collecting results.
Worker Process	A process responsible for executing an assigned portion of the computation.
Speedup	The ratio of sequential execution time to parallel execution time.
Parallel Efficiency	A measure of how effectively multiple processors are utilized.
Load Imbalance	A situation where different processors receive unequal amounts of work.
Communication Overhead	Time spent exchanging data between processes instead of performing computation.
Amdahl's Law	A law that calculates the theoretical maximum speedup based on the parallelizable portion of a program.