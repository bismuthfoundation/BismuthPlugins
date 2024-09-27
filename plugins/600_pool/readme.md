This is the very basic node plugin that is used to send new bloc data to eggpool.

# Why

Rather than modifying the node code, we rely on a plugin to extend Bis functionality, so we are update proof.

# Arch overview

The plugin hooks up to hte "new block" event, and relays the new block data to the pool and the stats management system.

In the eggpool context, as you'll see in the code, the data was transmitted twice:

- to the pool server itself, via a raw socket and the same protocol as used in Bis: len(msg) + msg.  
  the pool then formwarded it to the miners via a custom protocol and several distributed relays.
- to a SSDB instance (it's a persistent variant of REDIS, a key-value store), for real time reporting purposes.

The 'diff" hook wwas also taped, sent to the pool server only, so the pool know there is a diff drop and can mine lower difficulty blocks.

# Block inscription

The node ran with on-disk mempool, so the pool server could directly send the valid blocks to the sqlite db.  

# More insights

The various nodes of the pool are whitelisting each others so they remain sync. The relays between the pools and the miners are listening to all pool servers so they are able to always relay the best (freshest) block to mine asap, no matter which pool catches it first.
