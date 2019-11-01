rs.status(): 
```{
	"set" : "rs0",
	"date" : ISODate("2019-11-01T16:23:50.635Z"),
	"myState" : 1,
	"term" : NumberLong(1),
	"syncingTo" : "",
	"syncSourceHost" : "",
	"syncSourceId" : -1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572625422, 1),
			"t" : NumberLong(1)
		},
		"lastCommittedWallTime" : ISODate("2019-11-01T16:23:42.022Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572625422, 1),
			"t" : NumberLong(1)
		},
		"readConcernMajorityWallTime" : ISODate("2019-11-01T16:23:42.022Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572625422, 1),
			"t" : NumberLong(1)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572625422, 1),
			"t" : NumberLong(1)
		},
		"lastAppliedWallTime" : ISODate("2019-11-01T16:23:42.022Z"),
		"lastDurableWallTime" : ISODate("2019-11-01T16:23:42.022Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572625392, 1),
	"lastStableCheckpointTimestamp" : Timestamp(1572625392, 1),
	"electionCandidateMetrics" : {
		"lastElectionReason" : "electionTimeout",
		"lastElectionDate" : ISODate("2019-10-30T19:47:46.982Z"),
		"termAtElection" : NumberLong(1),
		"lastCommittedOpTimeAtElection" : {
			"ts" : Timestamp(0, 0),
			"t" : NumberLong(-1)
		},
		"lastSeenOpTimeAtElection" : {
			"ts" : Timestamp(1572464856, 1),
			"t" : NumberLong(-1)
		},
		"numVotesNeeded" : 2,
		"priorityAtElection" : 1,
		"electionTimeoutMillis" : NumberLong(10000),
		"numCatchUpOps" : NumberLong(2036470272),
		"newTermStartDate" : ISODate("2019-10-30T19:47:47.447Z"),
		"wMajorityWriteAvailabilityDate" : ISODate("2019-10-30T19:47:48.342Z")
	},
	"members" : [
		{
			"_id" : 0,
			"name" : "danisinst1.com:27017",
			"ip" : "172.31.46.153",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 160574,
			"optime" : {
				"ts" : Timestamp(1572625422, 1),
				"t" : NumberLong(1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572625422, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-11-01T16:23:42Z"),
			"optimeDurableDate" : ISODate("2019-11-01T16:23:42Z"),
			"lastHeartbeat" : ISODate("2019-11-01T16:23:49.006Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T16:23:49.006Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "danisinst2.com:27017",
			"syncSourceHost" : "danisinst2.com:27017",
			"syncSourceId" : 1,
			"infoMessage" : "",
			"configVersion" : 1
		},
		{
			"_id" : 1,
			"name" : "danisinst2.com:27017",
			"ip" : "172.31.41.153",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 161325,
			"optime" : {
				"ts" : Timestamp(1572625422, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-11-01T16:23:42Z"),
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"electionTime" : Timestamp(1572464866, 1),
			"electionDate" : ISODate("2019-10-30T19:47:46Z"),
			"configVersion" : 1,
			"self" : true,
			"lastHeartbeatMessage" : ""
		},
		{
			"_id" : 2,
			"name" : "danisinst3.com:27017",
			"ip" : "172.31.45.44",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 160574,
			"optime" : {
				"ts" : Timestamp(1572625422, 1),
				"t" : NumberLong(1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572625422, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-11-01T16:23:42Z"),
			"optimeDurableDate" : ISODate("2019-11-01T16:23:42Z"),
			"lastHeartbeat" : ISODate("2019-11-01T16:23:50.627Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T16:23:50.627Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "danisinst2.com:27017",
			"syncSourceHost" : "danisinst2.com:27017",
			"syncSourceId" : 1,
			"infoMessage" : "",
			"configVersion" : 1
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572625422, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572625422, 1)
}
```

rs.config():
```
{
	"_id" : "rs0",
	"version" : 1,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "danisinst1.com:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "danisinst2.com:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 2,
			"host" : "danisinst3.com:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {
			
		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("5db9e8d88b5b097ca1bc8d76")
	}
}
```
