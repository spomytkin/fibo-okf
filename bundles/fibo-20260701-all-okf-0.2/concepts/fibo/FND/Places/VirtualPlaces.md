---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology provides scaffolding for use in describing virtual location-oriented concepts.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2013-2025 EDM Council, Inc.\nCopyright (c) 2013-2025 Object Management Group, Inc.\n\nPermission\
      \ is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files\
      \ (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy,\
      \ modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom\
      \ the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission\
      \ notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED 'AS IS',\
      \ WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\
      \ FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE\
      \ FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT\
      \ OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\n\t\tSee https://opensource.org/licenses/MIT."
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Virtual Places Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The http://www.omg.org/spec/EDMC-FIBO/FND/20141101/Places/VirtualPlaces.rdf version of this ontology was modified
      for the FIBO 2.0 RFC to integrate it with LCC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Places/VirtualPlaces.rdf version of this ontology was
      modified to eliminate duplication of concepts in LCC and email address and telephone number.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200301/Places/VirtualPlaces.rdf version of this ontology was
      modified to address hygiene issues with respect to text formatting.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220301/Places/VirtualPlaces.rdf version of the ontology was
      modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata
      vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Places/VirtualPlaces.rdf version of this ontology was
      modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating
      redundancies in FIBO as appropriate, and to replace additional content that is now available in the OMG Commons Ontology
      Library (Commons) v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/Places/VirtualPlaces.rdf version of the ontology was
      modified to remove long deprecated elements (FND-399).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: This ontology was added to Foundations in advance of the December 2014 Long Beach meeting in support of the SEC
      specification.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/20251201/Places/VirtualPlaces/
  - concept: /concepts/fibo/FND/Places/Addresses.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Identifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Locations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Organizations/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/VirtualPlaces/
sources:
- id: fibo-source-408986d983
  resource: references/fibo/FND/Places/VirtualPlaces.rdf
  sha256: 408986d983df3f87901b90ff49e3ba3f323f94111338f7674037f481104e6007
  title: FIBO source FND/Places/VirtualPlaces.rdf
title: Virtual Places Ontology
type: Ontology Definition
---

# Virtual Places Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/VirtualPlaces/>

## Relationships

- **Related to**: [Addresses](/concepts/fibo/FND/Places/Addresses.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Identifiers](<https://www.omg.org/spec/Commons/Identifiers/>)
- **Related to**: [Locations](<https://www.omg.org/spec/Commons/Locations/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [VirtualPlaces](<https://spec.edmcouncil.org/fibo/ontology/FND/20251201/Places/VirtualPlaces/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology provides scaffolding for use in describing virtual location-oriented concepts.
- **license**: Copyright (c) 2013-2025 EDM Council, Inc. Copyright (c) 2013-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Virtual Places Ontology
- **changeNote**: The http://www.omg.org/spec/EDMC-FIBO/FND/20141101/Places/VirtualPlaces.rdf version of this ontology was modified for the FIBO 2.0 RFC to integrate it with LCC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Places/VirtualPlaces.rdf version of this ontology was modified to eliminate duplication of concepts in LCC and email address and telephone number.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200301/Places/VirtualPlaces.rdf version of this ontology was modified to address hygiene issues with respect to text formatting.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220301/Places/VirtualPlaces.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Places/VirtualPlaces.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate, and to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/Places/VirtualPlaces.rdf version of the ontology was modified to remove long deprecated elements (FND-399).
- **changeNote**: This ontology was added to Foundations in advance of the December 2014 Long Beach meeting in support of the SEC specification.
- **copyright**: Copyright (c) 2013-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2013-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
