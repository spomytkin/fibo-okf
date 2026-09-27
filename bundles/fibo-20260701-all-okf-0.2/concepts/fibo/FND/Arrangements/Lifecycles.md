---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines a set of basic concepts for lifecycles, including the various stages and events that make
      up a given lifecycle, for use in describing product, trade, instrument, production, and other lifecycles in FIBO.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://purl.org/dc/terms/license
    value: https://opensource.org/licenses/MIT
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Lifecycles Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Arrangements/Lifecycles.rdf version of this ontology
      was revised to replace hasDefinition with isDefinedIn to clarify intent.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190701/Arrangements/Lifecycles.rdf version of this ontology
      was revised to define lifecycle status, normalize definitions per ISO 704 and eliminate duplication with concepts in
      LCC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200201/Arrangements/Lifecycles.rdf version of this ontology
      was revised to add lifecycle stage as the superclass of maturity level.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200501/Arrangements/Lifecycles.rdf version of this ontology
      was revised to eliminate references to external dictionary sites that no longer resolve.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210101/Arrangements/Lifecycles.rdf version of the ontology
      was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Arrangements/Lifecycles.rdf version of this ontology
      was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC),
      eliminating redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/Arrangements/Lifecycles.rdf version of this ontology
      was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2017-2024 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2017-2024 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/20240101/Arrangements/Lifecycles/
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/
  - concept: /concepts/fibo/FND/Relations/Relations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Classifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/ContextualDesignators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Designators/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/
sources:
- id: fibo-source-92efc72f29
  resource: references/fibo/FND/Arrangements/Lifecycles.rdf
  sha256: 92efc72f29aba7c64208722174530078a5a46ad575d7ceabbf0cd9a444ad5e0e
  title: FIBO source FND/Arrangements/Lifecycles.rdf
title: Lifecycles Ontology
type: Ontology Definition
---

# Lifecycles Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/>

## Relationships

- **Related to**: [Occurrences](/concepts/fibo/FND/DatesAndTimes/Occurrences.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Classifiers](<https://www.omg.org/spec/Commons/Classifiers/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [ContextualDesignators](<https://www.omg.org/spec/Commons/ContextualDesignators/>)
- **Related to**: [Designators](<https://www.omg.org/spec/Commons/Designators/>)
- **Related to**: [Lifecycles](<https://spec.edmcouncil.org/fibo/ontology/FND/20240101/Arrangements/Lifecycles/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines a set of basic concepts for lifecycles, including the various stages and events that make up a given lifecycle, for use in describing product, trade, instrument, production, and other lifecycles in FIBO.
- **license**: https://opensource.org/licenses/MIT
- **label**: Lifecycles Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Arrangements/Lifecycles.rdf version of this ontology was revised to replace hasDefinition with isDefinedIn to clarify intent.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190701/Arrangements/Lifecycles.rdf version of this ontology was revised to define lifecycle status, normalize definitions per ISO 704 and eliminate duplication with concepts in LCC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200201/Arrangements/Lifecycles.rdf version of this ontology was revised to add lifecycle stage as the superclass of maturity level.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200501/Arrangements/Lifecycles.rdf version of this ontology was revised to eliminate references to external dictionary sites that no longer resolve.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210101/Arrangements/Lifecycles.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Arrangements/Lifecycles.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/Arrangements/Lifecycles.rdf version of this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **copyright**: Copyright (c) 2017-2024 EDM Council, Inc.
- **copyright**: Copyright (c) 2017-2024 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
