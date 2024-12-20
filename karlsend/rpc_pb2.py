# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpc.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\trpc.proto\x12\tprotowire\"\x1b\n\x08RPCError\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x9b\x01\n\x08RpcBlock\x12)\n\x06header\x18\x01 \x01(\x0b\x32\x19.protowire.RpcBlockHeader\x12/\n\x0ctransactions\x18\x02 \x03(\x0b\x32\x19.protowire.RpcTransaction\x12\x33\n\x0bverboseData\x18\x03 \x01(\x0b\x32\x1e.protowire.RpcBlockVerboseData\"\x9e\x02\n\x0eRpcBlockHeader\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x30\n\x07parents\x18\x0c \x03(\x0b\x32\x1f.protowire.RpcBlockLevelParents\x12\x16\n\x0ehashMerkleRoot\x18\x03 \x01(\t\x12\x1c\n\x14\x61\x63\x63\x65ptedIdMerkleRoot\x18\x04 \x01(\t\x12\x16\n\x0eutxoCommitment\x18\x05 \x01(\t\x12\x11\n\ttimestamp\x18\x06 \x01(\x03\x12\x0c\n\x04\x62its\x18\x07 \x01(\r\x12\r\n\x05nonce\x18\x08 \x01(\x04\x12\x10\n\x08\x64\x61\x61Score\x18\t \x01(\x04\x12\x10\n\x08\x62lueWork\x18\n \x01(\t\x12\x14\n\x0cpruningPoint\x18\x0e \x01(\t\x12\x11\n\tblueScore\x18\r \x01(\x04\",\n\x14RpcBlockLevelParents\x12\x14\n\x0cparentHashes\x18\x01 \x03(\t\"\xfb\x01\n\x13RpcBlockVerboseData\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12\x12\n\ndifficulty\x18\x0b \x01(\x01\x12\x1a\n\x12selectedParentHash\x18\r \x01(\t\x12\x16\n\x0etransactionIds\x18\x0e \x03(\t\x12\x14\n\x0cisHeaderOnly\x18\x0f \x01(\x08\x12\x11\n\tblueScore\x18\x10 \x01(\x04\x12\x16\n\x0e\x63hildrenHashes\x18\x11 \x03(\t\x12\x1b\n\x13mergeSetBluesHashes\x18\x12 \x03(\t\x12\x1a\n\x12mergeSetRedsHashes\x18\x13 \x03(\t\x12\x14\n\x0cisChainBlock\x18\x14 \x01(\x08\"\x92\x02\n\x0eRpcTransaction\x12\x0f\n\x07version\x18\x01 \x01(\r\x12.\n\x06inputs\x18\x02 \x03(\x0b\x32\x1e.protowire.RpcTransactionInput\x12\x30\n\x07outputs\x18\x03 \x03(\x0b\x32\x1f.protowire.RpcTransactionOutput\x12\x10\n\x08lockTime\x18\x04 \x01(\x04\x12\x14\n\x0csubnetworkId\x18\x05 \x01(\t\x12\x0b\n\x03gas\x18\x06 \x01(\x04\x12\x0f\n\x07payload\x18\x08 \x01(\t\x12\x39\n\x0bverboseData\x18\t \x01(\x0b\x32$.protowire.RpcTransactionVerboseData\x12\x0c\n\x04mass\x18\n \x01(\x04\"\xc6\x01\n\x13RpcTransactionInput\x12\x30\n\x10previousOutpoint\x18\x01 \x01(\x0b\x32\x16.protowire.RpcOutpoint\x12\x17\n\x0fsignatureScript\x18\x02 \x01(\t\x12\x10\n\x08sequence\x18\x03 \x01(\x04\x12\x12\n\nsigOpCount\x18\x05 \x01(\r\x12>\n\x0bverboseData\x18\x04 \x01(\x0b\x32).protowire.RpcTransactionInputVerboseData\">\n\x12RpcScriptPublicKey\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x17\n\x0fscriptPublicKey\x18\x02 \x01(\t\"\x9f\x01\n\x14RpcTransactionOutput\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x04\x12\x36\n\x0fscriptPublicKey\x18\x02 \x01(\x0b\x32\x1d.protowire.RpcScriptPublicKey\x12?\n\x0bverboseData\x18\x03 \x01(\x0b\x32*.protowire.RpcTransactionOutputVerboseData\"3\n\x0bRpcOutpoint\x12\x15\n\rtransactionId\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\r\"\x81\x01\n\x0cRpcUtxoEntry\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x04\x12\x36\n\x0fscriptPublicKey\x18\x02 \x01(\x0b\x32\x1d.protowire.RpcScriptPublicKey\x12\x15\n\rblockDaaScore\x18\x03 \x01(\x04\x12\x12\n\nisCoinbase\x18\x04 \x01(\x08\"t\n\x19RpcTransactionVerboseData\x12\x15\n\rtransactionId\x18\x01 \x01(\t\x12\x0c\n\x04hash\x18\x02 \x01(\t\x12\x0c\n\x04mass\x18\x04 \x01(\x04\x12\x11\n\tblockHash\x18\x0c \x01(\t\x12\x11\n\tblockTime\x18\x0e \x01(\x04\" \n\x1eRpcTransactionInputVerboseData\"^\n\x1fRpcTransactionOutputVerboseData\x12\x1b\n\x13scriptPublicKeyType\x18\x05 \x01(\t\x12\x1e\n\x16scriptPublicKeyAddress\x18\x06 \x01(\t\"!\n\x1fGetCurrentNetworkRequestMessage\"_\n GetCurrentNetworkResponseMessage\x12\x16\n\x0e\x63urrentNetwork\x18\x01 \x01(\t\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"Z\n\x19SubmitBlockRequestMessage\x12\"\n\x05\x62lock\x18\x02 \x01(\x0b\x32\x13.protowire.RpcBlock\x12\x19\n\x11\x61llowNonDAABlocks\x18\x03 \x01(\x08\"\xc7\x01\n\x1aSubmitBlockResponseMessage\x12H\n\x0crejectReason\x18\x01 \x01(\x0e\x32\x32.protowire.SubmitBlockResponseMessage.RejectReason\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\":\n\x0cRejectReason\x12\x08\n\x04NONE\x10\x00\x12\x11\n\rBLOCK_INVALID\x10\x01\x12\r\n\tIS_IN_IBD\x10\x02\"G\n\x1eGetBlockTemplateRequestMessage\x12\x12\n\npayAddress\x18\x01 \x01(\t\x12\x11\n\textraData\x18\x02 \x01(\t\"|\n\x1fGetBlockTemplateResponseMessage\x12\"\n\x05\x62lock\x18\x03 \x01(\x0b\x32\x13.protowire.RpcBlock\x12\x10\n\x08isSynced\x18\x02 \x01(\x08\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"N\n\x1eNotifyBlockAddedRequestMessage\x12,\n\x07\x63ommand\x18\x65 \x01(\x0e\x32\x1b.protowire.RpcNotifyCommand\"F\n\x1fNotifyBlockAddedResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"C\n\x1d\x42lockAddedNotificationMessage\x12\"\n\x05\x62lock\x18\x03 \x01(\x0b\x32\x13.protowire.RpcBlock\" \n\x1eGetPeerAddressesRequestMessage\"\xd2\x01\n\x1fGetPeerAddressesResponseMessage\x12\x41\n\taddresses\x18\x01 \x03(\x0b\x32..protowire.GetPeerAddressesKnownAddressMessage\x12G\n\x0f\x62\x61nnedAddresses\x18\x02 \x03(\x0b\x32..protowire.GetPeerAddressesKnownAddressMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"3\n#GetPeerAddressesKnownAddressMessage\x12\x0c\n\x04\x41\x64\x64r\x18\x01 \x01(\t\"\x17\n\x15GetSinkRequestMessage\"K\n\x16GetSinkResponseMessage\x12\x0c\n\x04sink\x18\x01 \x01(\t\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"g\n\x1dGetMempoolEntryRequestMessage\x12\x0c\n\x04txId\x18\x01 \x01(\t\x12\x19\n\x11includeOrphanPool\x18\x02 \x01(\x08\x12\x1d\n\x15\x66ilterTransactionPool\x18\x03 \x01(\x08\"p\n\x1eGetMempoolEntryResponseMessage\x12)\n\x05\x65ntry\x18\x01 \x01(\x0b\x32\x1a.protowire.RpcMempoolEntry\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"[\n\x1fGetMempoolEntriesRequestMessage\x12\x19\n\x11includeOrphanPool\x18\x01 \x01(\x08\x12\x1d\n\x15\x66ilterTransactionPool\x18\x02 \x01(\x08\"t\n GetMempoolEntriesResponseMessage\x12+\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x1a.protowire.RpcMempoolEntry\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"`\n\x0fRpcMempoolEntry\x12\x0b\n\x03\x66\x65\x65\x18\x01 \x01(\x04\x12.\n\x0btransaction\x18\x03 \x01(\x0b\x32\x19.protowire.RpcTransaction\x12\x10\n\x08isOrphan\x18\x04 \x01(\x08\"$\n\"GetConnectedPeerInfoRequestMessage\"\x81\x01\n#GetConnectedPeerInfoResponseMessage\x12\x35\n\x05infos\x18\x01 \x03(\x0b\x32&.protowire.GetConnectedPeerInfoMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"\xdc\x01\n\x1bGetConnectedPeerInfoMessage\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x18\n\x10lastPingDuration\x18\x03 \x01(\x03\x12\x12\n\nisOutbound\x18\x06 \x01(\x08\x12\x12\n\ntimeOffset\x18\x07 \x01(\x03\x12\x11\n\tuserAgent\x18\x08 \x01(\t\x12!\n\x19\x61\x64vertisedProtocolVersion\x18\t \x01(\r\x12\x15\n\rtimeConnected\x18\n \x01(\x03\x12\x11\n\tisIbdPeer\x18\x0b \x01(\x08\"=\n\x15\x41\x64\x64PeerRequestMessage\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x13\n\x0bisPermanent\x18\x02 \x01(\x08\"=\n\x16\x41\x64\x64PeerResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"f\n\x1fSubmitTransactionRequestMessage\x12.\n\x0btransaction\x18\x01 \x01(\x0b\x32\x19.protowire.RpcTransaction\x12\x13\n\x0b\x61llowOrphan\x18\x02 \x01(\x08\"^\n SubmitTransactionResponseMessage\x12\x15\n\rtransactionId\x18\x01 \x01(\t\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"~\n\'NotifyVirtualChainChangedRequestMessage\x12%\n\x1dincludeAcceptedTransactionIds\x18\x01 \x01(\x08\x12,\n\x07\x63ommand\x18\x65 \x01(\x0e\x32\x1b.protowire.RpcNotifyCommand\"O\n(NotifyVirtualChainChangedResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"\xae\x01\n&VirtualChainChangedNotificationMessage\x12\x1f\n\x17removedChainBlockHashes\x18\x01 \x03(\t\x12\x1d\n\x15\x61\x64\x64\x65\x64\x43hainBlockHashes\x18\x03 \x03(\t\x12\x44\n\x16\x61\x63\x63\x65ptedTransactionIds\x18\x02 \x03(\x0b\x32$.protowire.RpcAcceptedTransactionIds\"C\n\x16GetBlockRequestMessage\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12\x1b\n\x13includeTransactions\x18\x03 \x01(\x08\"b\n\x17GetBlockResponseMessage\x12\"\n\x05\x62lock\x18\x03 \x01(\x0b\x32\x13.protowire.RpcBlock\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"3\n\x1bGetSubnetworkRequestMessage\x12\x14\n\x0csubnetworkId\x18\x01 \x01(\t\"U\n\x1cGetSubnetworkResponseMessage\x12\x10\n\x08gasLimit\x18\x01 \x01(\x04\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"b\n&GetVirtualChainFromBlockRequestMessage\x12\x11\n\tstartHash\x18\x01 \x01(\t\x12%\n\x1dincludeAcceptedTransactionIds\x18\x02 \x01(\x08\"W\n\x19RpcAcceptedTransactionIds\x12\x1a\n\x12\x61\x63\x63\x65ptingBlockHash\x18\x01 \x01(\t\x12\x1e\n\x16\x61\x63\x63\x65ptedTransactionIds\x18\x02 \x03(\t\"\xd4\x01\n\'GetVirtualChainFromBlockResponseMessage\x12\x1f\n\x17removedChainBlockHashes\x18\x01 \x03(\t\x12\x1d\n\x15\x61\x64\x64\x65\x64\x43hainBlockHashes\x18\x03 \x03(\t\x12\x44\n\x16\x61\x63\x63\x65ptedTransactionIds\x18\x02 \x03(\x0b\x32$.protowire.RpcAcceptedTransactionIds\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"^\n\x17GetBlocksRequestMessage\x12\x0f\n\x07lowHash\x18\x01 \x01(\t\x12\x15\n\rincludeBlocks\x18\x02 \x01(\x08\x12\x1b\n\x13includeTransactions\x18\x03 \x01(\x08\"y\n\x18GetBlocksResponseMessage\x12\x13\n\x0b\x62lockHashes\x18\x04 \x03(\t\x12#\n\x06\x62locks\x18\x03 \x03(\x0b\x32\x13.protowire.RpcBlock\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"\x1d\n\x1bGetBlockCountRequestMessage\"l\n\x1cGetBlockCountResponseMessage\x12\x12\n\nblockCount\x18\x01 \x01(\x04\x12\x13\n\x0bheaderCount\x18\x02 \x01(\x04\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"\x1f\n\x1dGetBlockDagInfoRequestMessage\"\xa0\x02\n\x1eGetBlockDagInfoResponseMessage\x12\x13\n\x0bnetworkName\x18\x01 \x01(\t\x12\x12\n\nblockCount\x18\x02 \x01(\x04\x12\x13\n\x0bheaderCount\x18\x03 \x01(\x04\x12\x11\n\ttipHashes\x18\x04 \x03(\t\x12\x12\n\ndifficulty\x18\x05 \x01(\x01\x12\x16\n\x0epastMedianTime\x18\x06 \x01(\x03\x12\x1b\n\x13virtualParentHashes\x18\x07 \x03(\t\x12\x18\n\x10pruningPointHash\x18\x08 \x01(\t\x12\x17\n\x0fvirtualDaaScore\x18\t \x01(\x04\x12\x0c\n\x04sink\x18\n \x01(\t\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"B\n%ResolveFinalityConflictRequestMessage\x12\x19\n\x11\x66inalityBlockHash\x18\x01 \x01(\t\"M\n&ResolveFinalityConflictResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"T\n$NotifyFinalityConflictRequestMessage\x12,\n\x07\x63ommand\x18\x65 \x01(\x0e\x32\x1b.protowire.RpcNotifyCommand\"L\n%NotifyFinalityConflictResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"A\n#FinalityConflictNotificationMessage\x12\x1a\n\x12violatingBlockHash\x18\x01 \x01(\t\"H\n+FinalityConflictResolvedNotificationMessage\x12\x19\n\x11\x66inalityBlockHash\x18\x01 \x01(\t\"\x18\n\x16ShutdownRequestMessage\">\n\x17ShutdownResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"Q\n\x18GetHeadersRequestMessage\x12\x11\n\tstartHash\x18\x01 \x01(\t\x12\r\n\x05limit\x18\x02 \x01(\x04\x12\x13\n\x0bisAscending\x18\x03 \x01(\x08\"Q\n\x19GetHeadersResponseMessage\x12\x0f\n\x07headers\x18\x01 \x03(\t\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"c\n NotifyUtxosChangedRequestMessage\x12\x11\n\taddresses\x18\x01 \x03(\t\x12,\n\x07\x63ommand\x18\x65 \x01(\x0e\x32\x1b.protowire.RpcNotifyCommand\"H\n!NotifyUtxosChangedResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"\x8b\x01\n\x1fUtxosChangedNotificationMessage\x12\x32\n\x05\x61\x64\x64\x65\x64\x18\x01 \x03(\x0b\x32#.protowire.RpcUtxosByAddressesEntry\x12\x34\n\x07removed\x18\x02 \x03(\x0b\x32#.protowire.RpcUtxosByAddressesEntry\"\x81\x01\n\x18RpcUtxosByAddressesEntry\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12(\n\x08outpoint\x18\x02 \x01(\x0b\x32\x16.protowire.RpcOutpoint\x12*\n\tutxoEntry\x18\x03 \x01(\x0b\x32\x17.protowire.RpcUtxoEntry\"<\n\'StopNotifyingUtxosChangedRequestMessage\x12\x11\n\taddresses\x18\x01 \x03(\t\"O\n(StopNotifyingUtxosChangedResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"6\n!GetUtxosByAddressesRequestMessage\x12\x11\n\taddresses\x18\x01 \x03(\t\"\x7f\n\"GetUtxosByAddressesResponseMessage\x12\x34\n\x07\x65ntries\x18\x01 \x03(\x0b\x32#.protowire.RpcUtxosByAddressesEntry\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"4\n!GetBalanceByAddressRequestMessage\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"Z\n\"GetBalanceByAddressResponseMessage\x12\x0f\n\x07\x62\x61lance\x18\x01 \x01(\x04\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"9\n$GetBalancesByAddressesRequestMessage\x12\x11\n\taddresses\x18\x01 \x03(\t\"d\n\x1bRpcBalancesByAddressesEntry\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0f\n\x07\x62\x61lance\x18\x02 \x01(\x04\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"\x85\x01\n%GetBalancesByAddressesResponseMessage\x12\x37\n\x07\x65ntries\x18\x01 \x03(\x0b\x32&.protowire.RpcBalancesByAddressesEntry\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\" \n\x1eGetSinkBlueScoreRequestMessage\"Y\n\x1fGetSinkBlueScoreResponseMessage\x12\x11\n\tblueScore\x18\x01 \x01(\x04\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"X\n(NotifySinkBlueScoreChangedRequestMessage\x12,\n\x07\x63ommand\x18\x65 \x01(\x0e\x32\x1b.protowire.RpcNotifyCommand\"P\n)NotifySinkBlueScoreChangedResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"@\n\'SinkBlueScoreChangedNotificationMessage\x12\x15\n\rsinkBlueScore\x18\x01 \x01(\x04\"Z\n*NotifyVirtualDaaScoreChangedRequestMessage\x12,\n\x07\x63ommand\x18\x65 \x01(\x0e\x32\x1b.protowire.RpcNotifyCommand\"R\n+NotifyVirtualDaaScoreChangedResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"D\n)VirtualDaaScoreChangedNotificationMessage\x12\x17\n\x0fvirtualDaaScore\x18\x01 \x01(\x04\"_\n/NotifyPruningPointUtxoSetOverrideRequestMessage\x12,\n\x07\x63ommand\x18\x65 \x01(\x0e\x32\x1b.protowire.RpcNotifyCommand\"W\n0NotifyPruningPointUtxoSetOverrideResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"0\n.PruningPointUtxoSetOverrideNotificationMessage\"8\n6StopNotifyingPruningPointUtxoSetOverrideRequestMessage\"^\n7StopNotifyingPruningPointUtxoSetOverrideResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"\x1f\n\x11\x42\x61nRequestMessage\x12\n\n\x02ip\x18\x01 \x01(\t\"9\n\x12\x42\x61nResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"!\n\x13UnbanRequestMessage\x12\n\n\x02ip\x18\x01 \x01(\t\";\n\x14UnbanResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"\x17\n\x15GetInfoRequestMessage\"\xd1\x01\n\x16GetInfoResponseMessage\x12\r\n\x05p2pId\x18\x01 \x01(\t\x12\x13\n\x0bmempoolSize\x18\x02 \x01(\x04\x12\x15\n\rserverVersion\x18\x03 \x01(\t\x12\x15\n\risUtxoIndexed\x18\x04 \x01(\x08\x12\x10\n\x08isSynced\x18\x05 \x01(\x08\x12\x18\n\x10hasNotifyCommand\x18\x0b \x01(\x08\x12\x14\n\x0chasMessageId\x18\x0c \x01(\x08\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"U\n,EstimateNetworkHashesPerSecondRequestMessage\x12\x12\n\nwindowSize\x18\x01 \x01(\r\x12\x11\n\tstartHash\x18\x02 \x01(\t\"t\n-EstimateNetworkHashesPerSecondResponseMessage\x12\x1e\n\x16networkHashesPerSecond\x18\x01 \x01(\x04\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"T\n$NotifyNewBlockTemplateRequestMessage\x12,\n\x07\x63ommand\x18\x65 \x01(\x0e\x32\x1b.protowire.RpcNotifyCommand\"L\n%NotifyNewBlockTemplateResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"%\n#NewBlockTemplateNotificationMessage\"\x87\x01\n\x18RpcMempoolEntryByAddress\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12+\n\x07sending\x18\x02 \x03(\x0b\x32\x1a.protowire.RpcMempoolEntry\x12-\n\treceiving\x18\x03 \x03(\x0b\x32\x1a.protowire.RpcMempoolEntry\"y\n*GetMempoolEntriesByAddressesRequestMessage\x12\x11\n\taddresses\x18\x01 \x03(\t\x12\x19\n\x11includeOrphanPool\x18\x02 \x01(\x08\x12\x1d\n\x15\x66ilterTransactionPool\x18\x03 \x01(\x08\"\x88\x01\n+GetMempoolEntriesByAddressesResponseMessage\x12\x34\n\x07\x65ntries\x18\x01 \x03(\x0b\x32#.protowire.RpcMempoolEntryByAddress\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"\x1d\n\x1bGetCoinSupplyRequestMessage\"o\n\x1cGetCoinSupplyResponseMessage\x12\x10\n\x08maxSompi\x18\x01 \x01(\x04\x12\x18\n\x10\x63irculatingSompi\x18\x02 \x01(\x04\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"\x14\n\x12PingRequestMessage\":\n\x13PingResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"\xde\x01\n\x0eProcessMetrics\x12\x17\n\x0fresidentSetSize\x18\x01 \x01(\x04\x12\x19\n\x11virtualMemorySize\x18\x02 \x01(\x04\x12\x0f\n\x07\x63oreNum\x18\x03 \x01(\r\x12\x10\n\x08\x63puUsage\x18\x04 \x01(\x02\x12\r\n\x05\x66\x64Num\x18\x05 \x01(\r\x12\x17\n\x0f\x64iskIoReadBytes\x18\x06 \x01(\x04\x12\x18\n\x10\x64iskIoWriteBytes\x18\x07 \x01(\x04\x12\x18\n\x10\x64iskIoReadPerSec\x18\x08 \x01(\x02\x12\x19\n\x11\x64iskIoWritePerSec\x18\t \x01(\x02\"\xe3\x01\n\x11\x43onnectionMetrics\x12\x1c\n\x14\x62orshLiveConnections\x18\x1f \x01(\r\x12\x1f\n\x17\x62orshConnectionAttempts\x18  \x01(\x04\x12\x1e\n\x16\x62orshHandshakeFailures\x18! \x01(\x04\x12\x1b\n\x13jsonLiveConnections\x18) \x01(\r\x12\x1e\n\x16jsonConnectionAttempts\x18* \x01(\x04\x12\x1d\n\x15jsonHandshakeFailures\x18+ \x01(\x04\x12\x13\n\x0b\x61\x63tivePeers\x18\x33 \x01(\r\"\xca\x01\n\x10\x42\x61ndwidthMetrics\x12\x14\n\x0c\x62orshBytesTx\x18= \x01(\x04\x12\x14\n\x0c\x62orshBytesRx\x18> \x01(\x04\x12\x13\n\x0bjsonBytesTx\x18? \x01(\x04\x12\x13\n\x0bjsonBytesRx\x18@ \x01(\x04\x12\x16\n\x0egrpcP2pBytesTx\x18\x41 \x01(\x04\x12\x16\n\x0egrpcP2pBytesRx\x18\x42 \x01(\x04\x12\x17\n\x0fgrpcUserBytesTx\x18\x43 \x01(\x04\x12\x17\n\x0fgrpcUserBytesRx\x18\x44 \x01(\x04\"\xe6\x02\n\x10\x43onsensusMetrics\x12\x17\n\x0f\x62locksSubmitted\x18\x01 \x01(\x04\x12\x14\n\x0cheaderCounts\x18\x02 \x01(\x04\x12\x11\n\tdepCounts\x18\x03 \x01(\x04\x12\x12\n\nbodyCounts\x18\x04 \x01(\x04\x12\x11\n\ttxsCounts\x18\x05 \x01(\x04\x12\x18\n\x10\x63hainBlockCounts\x18\x06 \x01(\x04\x12\x12\n\nmassCounts\x18\x07 \x01(\x04\x12\x12\n\nblockCount\x18\x0b \x01(\x04\x12\x13\n\x0bheaderCount\x18\x0c \x01(\x04\x12\x13\n\x0bmempoolSize\x18\r \x01(\x04\x12\x16\n\x0etipHashesCount\x18\x0e \x01(\r\x12\x12\n\ndifficulty\x18\x0f \x01(\x01\x12\x16\n\x0epastMedianTime\x18\x10 \x01(\x04\x12 \n\x18virtualParentHashesCount\x18\x11 \x01(\r\x12\x17\n\x0fvirtualDaaScore\x18\x12 \x01(\x04\"\x81\x01\n\x18GetMetricsRequestMessage\x12\x16\n\x0eprocessMetrics\x18\x01 \x01(\x08\x12\x19\n\x11\x63onnectionMetrics\x18\x02 \x01(\x08\x12\x18\n\x10\x62\x61ndwidthMetrics\x18\x03 \x01(\x08\x12\x18\n\x10\x63onsensusMetrics\x18\x04 \x01(\x08\"\xae\x02\n\x19GetMetricsResponseMessage\x12\x12\n\nserverTime\x18\x01 \x01(\x04\x12\x31\n\x0eprocessMetrics\x18\x0b \x01(\x0b\x32\x19.protowire.ProcessMetrics\x12\x37\n\x11\x63onnectionMetrics\x18\x0c \x01(\x0b\x32\x1c.protowire.ConnectionMetrics\x12\x35\n\x10\x62\x61ndwidthMetrics\x18\r \x01(\x0b\x32\x1b.protowire.BandwidthMetrics\x12\x35\n\x10\x63onsensusMetrics\x18\x0e \x01(\x0b\x32\x1b.protowire.ConsensusMetrics\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"\x1d\n\x1bGetServerInfoRequestMessage\"\xc5\x01\n\x1cGetServerInfoResponseMessage\x12\x15\n\rrpcApiVersion\x18\x01 \x03(\r\x12\x15\n\rserverVersion\x18\x02 \x01(\t\x12\x11\n\tnetworkId\x18\x03 \x01(\t\x12\x14\n\x0chasUtxoIndex\x18\x04 \x01(\x08\x12\x10\n\x08isSynced\x18\x05 \x01(\x08\x12\x17\n\x0fvirtualDaaScore\x18\x06 \x01(\x04\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"\x1d\n\x1bGetSyncStatusRequestMessage\"U\n\x1cGetSyncStatusResponseMessage\x12\x10\n\x08isSynced\x18\x01 \x01(\x08\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"@\n*GetDaaScoreTimestampEstimateRequestMessage\x12\x12\n\ndaa_scores\x18\x01 \x03(\x04\"f\n+GetDaaScoreTimestampEstimateResponseMessage\x12\x12\n\ntimestamps\x18\x01 \x03(\x04\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError*5\n\x10RpcNotifyCommand\x12\x10\n\x0cNOTIFY_START\x10\x00\x12\x0f\n\x0bNOTIFY_STOP\x10\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'rpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_RPCNOTIFYCOMMAND']._serialized_start=12578
  _globals['_RPCNOTIFYCOMMAND']._serialized_end=12631
  _globals['_RPCERROR']._serialized_start=24
  _globals['_RPCERROR']._serialized_end=51
  _globals['_RPCBLOCK']._serialized_start=54
  _globals['_RPCBLOCK']._serialized_end=209
  _globals['_RPCBLOCKHEADER']._serialized_start=212
  _globals['_RPCBLOCKHEADER']._serialized_end=498
  _globals['_RPCBLOCKLEVELPARENTS']._serialized_start=500
  _globals['_RPCBLOCKLEVELPARENTS']._serialized_end=544
  _globals['_RPCBLOCKVERBOSEDATA']._serialized_start=547
  _globals['_RPCBLOCKVERBOSEDATA']._serialized_end=798
  _globals['_RPCTRANSACTION']._serialized_start=801
  _globals['_RPCTRANSACTION']._serialized_end=1075
  _globals['_RPCTRANSACTIONINPUT']._serialized_start=1078
  _globals['_RPCTRANSACTIONINPUT']._serialized_end=1276
  _globals['_RPCSCRIPTPUBLICKEY']._serialized_start=1278
  _globals['_RPCSCRIPTPUBLICKEY']._serialized_end=1340
  _globals['_RPCTRANSACTIONOUTPUT']._serialized_start=1343
  _globals['_RPCTRANSACTIONOUTPUT']._serialized_end=1502
  _globals['_RPCOUTPOINT']._serialized_start=1504
  _globals['_RPCOUTPOINT']._serialized_end=1555
  _globals['_RPCUTXOENTRY']._serialized_start=1558
  _globals['_RPCUTXOENTRY']._serialized_end=1687
  _globals['_RPCTRANSACTIONVERBOSEDATA']._serialized_start=1689
  _globals['_RPCTRANSACTIONVERBOSEDATA']._serialized_end=1805
  _globals['_RPCTRANSACTIONINPUTVERBOSEDATA']._serialized_start=1807
  _globals['_RPCTRANSACTIONINPUTVERBOSEDATA']._serialized_end=1839
  _globals['_RPCTRANSACTIONOUTPUTVERBOSEDATA']._serialized_start=1841
  _globals['_RPCTRANSACTIONOUTPUTVERBOSEDATA']._serialized_end=1935
  _globals['_GETCURRENTNETWORKREQUESTMESSAGE']._serialized_start=1937
  _globals['_GETCURRENTNETWORKREQUESTMESSAGE']._serialized_end=1970
  _globals['_GETCURRENTNETWORKRESPONSEMESSAGE']._serialized_start=1972
  _globals['_GETCURRENTNETWORKRESPONSEMESSAGE']._serialized_end=2067
  _globals['_SUBMITBLOCKREQUESTMESSAGE']._serialized_start=2069
  _globals['_SUBMITBLOCKREQUESTMESSAGE']._serialized_end=2159
  _globals['_SUBMITBLOCKRESPONSEMESSAGE']._serialized_start=2162
  _globals['_SUBMITBLOCKRESPONSEMESSAGE']._serialized_end=2361
  _globals['_SUBMITBLOCKRESPONSEMESSAGE_REJECTREASON']._serialized_start=2303
  _globals['_SUBMITBLOCKRESPONSEMESSAGE_REJECTREASON']._serialized_end=2361
  _globals['_GETBLOCKTEMPLATEREQUESTMESSAGE']._serialized_start=2363
  _globals['_GETBLOCKTEMPLATEREQUESTMESSAGE']._serialized_end=2434
  _globals['_GETBLOCKTEMPLATERESPONSEMESSAGE']._serialized_start=2436
  _globals['_GETBLOCKTEMPLATERESPONSEMESSAGE']._serialized_end=2560
  _globals['_NOTIFYBLOCKADDEDREQUESTMESSAGE']._serialized_start=2562
  _globals['_NOTIFYBLOCKADDEDREQUESTMESSAGE']._serialized_end=2640
  _globals['_NOTIFYBLOCKADDEDRESPONSEMESSAGE']._serialized_start=2642
  _globals['_NOTIFYBLOCKADDEDRESPONSEMESSAGE']._serialized_end=2712
  _globals['_BLOCKADDEDNOTIFICATIONMESSAGE']._serialized_start=2714
  _globals['_BLOCKADDEDNOTIFICATIONMESSAGE']._serialized_end=2781
  _globals['_GETPEERADDRESSESREQUESTMESSAGE']._serialized_start=2783
  _globals['_GETPEERADDRESSESREQUESTMESSAGE']._serialized_end=2815
  _globals['_GETPEERADDRESSESRESPONSEMESSAGE']._serialized_start=2818
  _globals['_GETPEERADDRESSESRESPONSEMESSAGE']._serialized_end=3028
  _globals['_GETPEERADDRESSESKNOWNADDRESSMESSAGE']._serialized_start=3030
  _globals['_GETPEERADDRESSESKNOWNADDRESSMESSAGE']._serialized_end=3081
  _globals['_GETSINKREQUESTMESSAGE']._serialized_start=3083
  _globals['_GETSINKREQUESTMESSAGE']._serialized_end=3106
  _globals['_GETSINKRESPONSEMESSAGE']._serialized_start=3108
  _globals['_GETSINKRESPONSEMESSAGE']._serialized_end=3183
  _globals['_GETMEMPOOLENTRYREQUESTMESSAGE']._serialized_start=3185
  _globals['_GETMEMPOOLENTRYREQUESTMESSAGE']._serialized_end=3288
  _globals['_GETMEMPOOLENTRYRESPONSEMESSAGE']._serialized_start=3290
  _globals['_GETMEMPOOLENTRYRESPONSEMESSAGE']._serialized_end=3402
  _globals['_GETMEMPOOLENTRIESREQUESTMESSAGE']._serialized_start=3404
  _globals['_GETMEMPOOLENTRIESREQUESTMESSAGE']._serialized_end=3495
  _globals['_GETMEMPOOLENTRIESRESPONSEMESSAGE']._serialized_start=3497
  _globals['_GETMEMPOOLENTRIESRESPONSEMESSAGE']._serialized_end=3613
  _globals['_RPCMEMPOOLENTRY']._serialized_start=3615
  _globals['_RPCMEMPOOLENTRY']._serialized_end=3711
  _globals['_GETCONNECTEDPEERINFOREQUESTMESSAGE']._serialized_start=3713
  _globals['_GETCONNECTEDPEERINFOREQUESTMESSAGE']._serialized_end=3749
  _globals['_GETCONNECTEDPEERINFORESPONSEMESSAGE']._serialized_start=3752
  _globals['_GETCONNECTEDPEERINFORESPONSEMESSAGE']._serialized_end=3881
  _globals['_GETCONNECTEDPEERINFOMESSAGE']._serialized_start=3884
  _globals['_GETCONNECTEDPEERINFOMESSAGE']._serialized_end=4104
  _globals['_ADDPEERREQUESTMESSAGE']._serialized_start=4106
  _globals['_ADDPEERREQUESTMESSAGE']._serialized_end=4167
  _globals['_ADDPEERRESPONSEMESSAGE']._serialized_start=4169
  _globals['_ADDPEERRESPONSEMESSAGE']._serialized_end=4230
  _globals['_SUBMITTRANSACTIONREQUESTMESSAGE']._serialized_start=4232
  _globals['_SUBMITTRANSACTIONREQUESTMESSAGE']._serialized_end=4334
  _globals['_SUBMITTRANSACTIONRESPONSEMESSAGE']._serialized_start=4336
  _globals['_SUBMITTRANSACTIONRESPONSEMESSAGE']._serialized_end=4430
  _globals['_NOTIFYVIRTUALCHAINCHANGEDREQUESTMESSAGE']._serialized_start=4432
  _globals['_NOTIFYVIRTUALCHAINCHANGEDREQUESTMESSAGE']._serialized_end=4558
  _globals['_NOTIFYVIRTUALCHAINCHANGEDRESPONSEMESSAGE']._serialized_start=4560
  _globals['_NOTIFYVIRTUALCHAINCHANGEDRESPONSEMESSAGE']._serialized_end=4639
  _globals['_VIRTUALCHAINCHANGEDNOTIFICATIONMESSAGE']._serialized_start=4642
  _globals['_VIRTUALCHAINCHANGEDNOTIFICATIONMESSAGE']._serialized_end=4816
  _globals['_GETBLOCKREQUESTMESSAGE']._serialized_start=4818
  _globals['_GETBLOCKREQUESTMESSAGE']._serialized_end=4885
  _globals['_GETBLOCKRESPONSEMESSAGE']._serialized_start=4887
  _globals['_GETBLOCKRESPONSEMESSAGE']._serialized_end=4985
  _globals['_GETSUBNETWORKREQUESTMESSAGE']._serialized_start=4987
  _globals['_GETSUBNETWORKREQUESTMESSAGE']._serialized_end=5038
  _globals['_GETSUBNETWORKRESPONSEMESSAGE']._serialized_start=5040
  _globals['_GETSUBNETWORKRESPONSEMESSAGE']._serialized_end=5125
  _globals['_GETVIRTUALCHAINFROMBLOCKREQUESTMESSAGE']._serialized_start=5127
  _globals['_GETVIRTUALCHAINFROMBLOCKREQUESTMESSAGE']._serialized_end=5225
  _globals['_RPCACCEPTEDTRANSACTIONIDS']._serialized_start=5227
  _globals['_RPCACCEPTEDTRANSACTIONIDS']._serialized_end=5314
  _globals['_GETVIRTUALCHAINFROMBLOCKRESPONSEMESSAGE']._serialized_start=5317
  _globals['_GETVIRTUALCHAINFROMBLOCKRESPONSEMESSAGE']._serialized_end=5529
  _globals['_GETBLOCKSREQUESTMESSAGE']._serialized_start=5531
  _globals['_GETBLOCKSREQUESTMESSAGE']._serialized_end=5625
  _globals['_GETBLOCKSRESPONSEMESSAGE']._serialized_start=5627
  _globals['_GETBLOCKSRESPONSEMESSAGE']._serialized_end=5748
  _globals['_GETBLOCKCOUNTREQUESTMESSAGE']._serialized_start=5750
  _globals['_GETBLOCKCOUNTREQUESTMESSAGE']._serialized_end=5779
  _globals['_GETBLOCKCOUNTRESPONSEMESSAGE']._serialized_start=5781
  _globals['_GETBLOCKCOUNTRESPONSEMESSAGE']._serialized_end=5889
  _globals['_GETBLOCKDAGINFOREQUESTMESSAGE']._serialized_start=5891
  _globals['_GETBLOCKDAGINFOREQUESTMESSAGE']._serialized_end=5922
  _globals['_GETBLOCKDAGINFORESPONSEMESSAGE']._serialized_start=5925
  _globals['_GETBLOCKDAGINFORESPONSEMESSAGE']._serialized_end=6213
  _globals['_RESOLVEFINALITYCONFLICTREQUESTMESSAGE']._serialized_start=6215
  _globals['_RESOLVEFINALITYCONFLICTREQUESTMESSAGE']._serialized_end=6281
  _globals['_RESOLVEFINALITYCONFLICTRESPONSEMESSAGE']._serialized_start=6283
  _globals['_RESOLVEFINALITYCONFLICTRESPONSEMESSAGE']._serialized_end=6360
  _globals['_NOTIFYFINALITYCONFLICTREQUESTMESSAGE']._serialized_start=6362
  _globals['_NOTIFYFINALITYCONFLICTREQUESTMESSAGE']._serialized_end=6446
  _globals['_NOTIFYFINALITYCONFLICTRESPONSEMESSAGE']._serialized_start=6448
  _globals['_NOTIFYFINALITYCONFLICTRESPONSEMESSAGE']._serialized_end=6524
  _globals['_FINALITYCONFLICTNOTIFICATIONMESSAGE']._serialized_start=6526
  _globals['_FINALITYCONFLICTNOTIFICATIONMESSAGE']._serialized_end=6591
  _globals['_FINALITYCONFLICTRESOLVEDNOTIFICATIONMESSAGE']._serialized_start=6593
  _globals['_FINALITYCONFLICTRESOLVEDNOTIFICATIONMESSAGE']._serialized_end=6665
  _globals['_SHUTDOWNREQUESTMESSAGE']._serialized_start=6667
  _globals['_SHUTDOWNREQUESTMESSAGE']._serialized_end=6691
  _globals['_SHUTDOWNRESPONSEMESSAGE']._serialized_start=6693
  _globals['_SHUTDOWNRESPONSEMESSAGE']._serialized_end=6755
  _globals['_GETHEADERSREQUESTMESSAGE']._serialized_start=6757
  _globals['_GETHEADERSREQUESTMESSAGE']._serialized_end=6838
  _globals['_GETHEADERSRESPONSEMESSAGE']._serialized_start=6840
  _globals['_GETHEADERSRESPONSEMESSAGE']._serialized_end=6921
  _globals['_NOTIFYUTXOSCHANGEDREQUESTMESSAGE']._serialized_start=6923
  _globals['_NOTIFYUTXOSCHANGEDREQUESTMESSAGE']._serialized_end=7022
  _globals['_NOTIFYUTXOSCHANGEDRESPONSEMESSAGE']._serialized_start=7024
  _globals['_NOTIFYUTXOSCHANGEDRESPONSEMESSAGE']._serialized_end=7096
  _globals['_UTXOSCHANGEDNOTIFICATIONMESSAGE']._serialized_start=7099
  _globals['_UTXOSCHANGEDNOTIFICATIONMESSAGE']._serialized_end=7238
  _globals['_RPCUTXOSBYADDRESSESENTRY']._serialized_start=7241
  _globals['_RPCUTXOSBYADDRESSESENTRY']._serialized_end=7370
  _globals['_STOPNOTIFYINGUTXOSCHANGEDREQUESTMESSAGE']._serialized_start=7372
  _globals['_STOPNOTIFYINGUTXOSCHANGEDREQUESTMESSAGE']._serialized_end=7432
  _globals['_STOPNOTIFYINGUTXOSCHANGEDRESPONSEMESSAGE']._serialized_start=7434
  _globals['_STOPNOTIFYINGUTXOSCHANGEDRESPONSEMESSAGE']._serialized_end=7513
  _globals['_GETUTXOSBYADDRESSESREQUESTMESSAGE']._serialized_start=7515
  _globals['_GETUTXOSBYADDRESSESREQUESTMESSAGE']._serialized_end=7569
  _globals['_GETUTXOSBYADDRESSESRESPONSEMESSAGE']._serialized_start=7571
  _globals['_GETUTXOSBYADDRESSESRESPONSEMESSAGE']._serialized_end=7698
  _globals['_GETBALANCEBYADDRESSREQUESTMESSAGE']._serialized_start=7700
  _globals['_GETBALANCEBYADDRESSREQUESTMESSAGE']._serialized_end=7752
  _globals['_GETBALANCEBYADDRESSRESPONSEMESSAGE']._serialized_start=7754
  _globals['_GETBALANCEBYADDRESSRESPONSEMESSAGE']._serialized_end=7844
  _globals['_GETBALANCESBYADDRESSESREQUESTMESSAGE']._serialized_start=7846
  _globals['_GETBALANCESBYADDRESSESREQUESTMESSAGE']._serialized_end=7903
  _globals['_RPCBALANCESBYADDRESSESENTRY']._serialized_start=7905
  _globals['_RPCBALANCESBYADDRESSESENTRY']._serialized_end=8005
  _globals['_GETBALANCESBYADDRESSESRESPONSEMESSAGE']._serialized_start=8008
  _globals['_GETBALANCESBYADDRESSESRESPONSEMESSAGE']._serialized_end=8141
  _globals['_GETSINKBLUESCOREREQUESTMESSAGE']._serialized_start=8143
  _globals['_GETSINKBLUESCOREREQUESTMESSAGE']._serialized_end=8175
  _globals['_GETSINKBLUESCORERESPONSEMESSAGE']._serialized_start=8177
  _globals['_GETSINKBLUESCORERESPONSEMESSAGE']._serialized_end=8266
  _globals['_NOTIFYSINKBLUESCORECHANGEDREQUESTMESSAGE']._serialized_start=8268
  _globals['_NOTIFYSINKBLUESCORECHANGEDREQUESTMESSAGE']._serialized_end=8356
  _globals['_NOTIFYSINKBLUESCORECHANGEDRESPONSEMESSAGE']._serialized_start=8358
  _globals['_NOTIFYSINKBLUESCORECHANGEDRESPONSEMESSAGE']._serialized_end=8438
  _globals['_SINKBLUESCORECHANGEDNOTIFICATIONMESSAGE']._serialized_start=8440
  _globals['_SINKBLUESCORECHANGEDNOTIFICATIONMESSAGE']._serialized_end=8504
  _globals['_NOTIFYVIRTUALDAASCORECHANGEDREQUESTMESSAGE']._serialized_start=8506
  _globals['_NOTIFYVIRTUALDAASCORECHANGEDREQUESTMESSAGE']._serialized_end=8596
  _globals['_NOTIFYVIRTUALDAASCORECHANGEDRESPONSEMESSAGE']._serialized_start=8598
  _globals['_NOTIFYVIRTUALDAASCORECHANGEDRESPONSEMESSAGE']._serialized_end=8680
  _globals['_VIRTUALDAASCORECHANGEDNOTIFICATIONMESSAGE']._serialized_start=8682
  _globals['_VIRTUALDAASCORECHANGEDNOTIFICATIONMESSAGE']._serialized_end=8750
  _globals['_NOTIFYPRUNINGPOINTUTXOSETOVERRIDEREQUESTMESSAGE']._serialized_start=8752
  _globals['_NOTIFYPRUNINGPOINTUTXOSETOVERRIDEREQUESTMESSAGE']._serialized_end=8847
  _globals['_NOTIFYPRUNINGPOINTUTXOSETOVERRIDERESPONSEMESSAGE']._serialized_start=8849
  _globals['_NOTIFYPRUNINGPOINTUTXOSETOVERRIDERESPONSEMESSAGE']._serialized_end=8936
  _globals['_PRUNINGPOINTUTXOSETOVERRIDENOTIFICATIONMESSAGE']._serialized_start=8938
  _globals['_PRUNINGPOINTUTXOSETOVERRIDENOTIFICATIONMESSAGE']._serialized_end=8986
  _globals['_STOPNOTIFYINGPRUNINGPOINTUTXOSETOVERRIDEREQUESTMESSAGE']._serialized_start=8988
  _globals['_STOPNOTIFYINGPRUNINGPOINTUTXOSETOVERRIDEREQUESTMESSAGE']._serialized_end=9044
  _globals['_STOPNOTIFYINGPRUNINGPOINTUTXOSETOVERRIDERESPONSEMESSAGE']._serialized_start=9046
  _globals['_STOPNOTIFYINGPRUNINGPOINTUTXOSETOVERRIDERESPONSEMESSAGE']._serialized_end=9140
  _globals['_BANREQUESTMESSAGE']._serialized_start=9142
  _globals['_BANREQUESTMESSAGE']._serialized_end=9173
  _globals['_BANRESPONSEMESSAGE']._serialized_start=9175
  _globals['_BANRESPONSEMESSAGE']._serialized_end=9232
  _globals['_UNBANREQUESTMESSAGE']._serialized_start=9234
  _globals['_UNBANREQUESTMESSAGE']._serialized_end=9267
  _globals['_UNBANRESPONSEMESSAGE']._serialized_start=9269
  _globals['_UNBANRESPONSEMESSAGE']._serialized_end=9328
  _globals['_GETINFOREQUESTMESSAGE']._serialized_start=9330
  _globals['_GETINFOREQUESTMESSAGE']._serialized_end=9353
  _globals['_GETINFORESPONSEMESSAGE']._serialized_start=9356
  _globals['_GETINFORESPONSEMESSAGE']._serialized_end=9565
  _globals['_ESTIMATENETWORKHASHESPERSECONDREQUESTMESSAGE']._serialized_start=9567
  _globals['_ESTIMATENETWORKHASHESPERSECONDREQUESTMESSAGE']._serialized_end=9652
  _globals['_ESTIMATENETWORKHASHESPERSECONDRESPONSEMESSAGE']._serialized_start=9654
  _globals['_ESTIMATENETWORKHASHESPERSECONDRESPONSEMESSAGE']._serialized_end=9770
  _globals['_NOTIFYNEWBLOCKTEMPLATEREQUESTMESSAGE']._serialized_start=9772
  _globals['_NOTIFYNEWBLOCKTEMPLATEREQUESTMESSAGE']._serialized_end=9856
  _globals['_NOTIFYNEWBLOCKTEMPLATERESPONSEMESSAGE']._serialized_start=9858
  _globals['_NOTIFYNEWBLOCKTEMPLATERESPONSEMESSAGE']._serialized_end=9934
  _globals['_NEWBLOCKTEMPLATENOTIFICATIONMESSAGE']._serialized_start=9936
  _globals['_NEWBLOCKTEMPLATENOTIFICATIONMESSAGE']._serialized_end=9973
  _globals['_RPCMEMPOOLENTRYBYADDRESS']._serialized_start=9976
  _globals['_RPCMEMPOOLENTRYBYADDRESS']._serialized_end=10111
  _globals['_GETMEMPOOLENTRIESBYADDRESSESREQUESTMESSAGE']._serialized_start=10113
  _globals['_GETMEMPOOLENTRIESBYADDRESSESREQUESTMESSAGE']._serialized_end=10234
  _globals['_GETMEMPOOLENTRIESBYADDRESSESRESPONSEMESSAGE']._serialized_start=10237
  _globals['_GETMEMPOOLENTRIESBYADDRESSESRESPONSEMESSAGE']._serialized_end=10373
  _globals['_GETCOINSUPPLYREQUESTMESSAGE']._serialized_start=10375
  _globals['_GETCOINSUPPLYREQUESTMESSAGE']._serialized_end=10404
  _globals['_GETCOINSUPPLYRESPONSEMESSAGE']._serialized_start=10406
  _globals['_GETCOINSUPPLYRESPONSEMESSAGE']._serialized_end=10517
  _globals['_PINGREQUESTMESSAGE']._serialized_start=10519
  _globals['_PINGREQUESTMESSAGE']._serialized_end=10539
  _globals['_PINGRESPONSEMESSAGE']._serialized_start=10541
  _globals['_PINGRESPONSEMESSAGE']._serialized_end=10599
  _globals['_PROCESSMETRICS']._serialized_start=10602
  _globals['_PROCESSMETRICS']._serialized_end=10824
  _globals['_CONNECTIONMETRICS']._serialized_start=10827
  _globals['_CONNECTIONMETRICS']._serialized_end=11054
  _globals['_BANDWIDTHMETRICS']._serialized_start=11057
  _globals['_BANDWIDTHMETRICS']._serialized_end=11259
  _globals['_CONSENSUSMETRICS']._serialized_start=11262
  _globals['_CONSENSUSMETRICS']._serialized_end=11620
  _globals['_GETMETRICSREQUESTMESSAGE']._serialized_start=11623
  _globals['_GETMETRICSREQUESTMESSAGE']._serialized_end=11752
  _globals['_GETMETRICSRESPONSEMESSAGE']._serialized_start=11755
  _globals['_GETMETRICSRESPONSEMESSAGE']._serialized_end=12057
  _globals['_GETSERVERINFOREQUESTMESSAGE']._serialized_start=12059
  _globals['_GETSERVERINFOREQUESTMESSAGE']._serialized_end=12088
  _globals['_GETSERVERINFORESPONSEMESSAGE']._serialized_start=12091
  _globals['_GETSERVERINFORESPONSEMESSAGE']._serialized_end=12288
  _globals['_GETSYNCSTATUSREQUESTMESSAGE']._serialized_start=12290
  _globals['_GETSYNCSTATUSREQUESTMESSAGE']._serialized_end=12319
  _globals['_GETSYNCSTATUSRESPONSEMESSAGE']._serialized_start=12321
  _globals['_GETSYNCSTATUSRESPONSEMESSAGE']._serialized_end=12406
  _globals['_GETDAASCORETIMESTAMPESTIMATEREQUESTMESSAGE']._serialized_start=12408
  _globals['_GETDAASCORETIMESTAMPESTIMATEREQUESTMESSAGE']._serialized_end=12472
  _globals['_GETDAASCORETIMESTAMPESTIMATERESPONSEMESSAGE']._serialized_start=12474
  _globals['_GETDAASCORETIMESTAMPESTIMATERESPONSEMESSAGE']._serialized_end=12576
# @@protoc_insertion_point(module_scope)
