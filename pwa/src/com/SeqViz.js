import React from 'react';
import { SeqViz } from 'seqviz';

const SequenceViewer = () => (
  <SeqViz
    name="J23100"
    seq="TTGACGGCTAGCTCAGTCCTAGGTACAGTGCTAGC"
    annotations={[
      {
        name: "promoter",
        start: 0,
        end: 34,
        direction: 1,
        color: "blue",
      },
    ]}
  />
);

export default SequenceViewer;
