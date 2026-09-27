---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines abstract concepts for representation of industry classification schemes.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://purl.org/dc/terms/license
    value: https://opensource.org/licenses/MIT
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Classification Schemes Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20150501/Arrangements/ClassificationSchemes.rdf version of this
      ontology was introduced as a part of the initial FIBO FBC RFC and revised due to changes introduced in the FIBO 2.0
      RFC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Arrangements/ClassificationSchemes.rdf version of this
      ontology was revised to replace hasDefinition with isDefinedIn to clarify intent.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190701/Arrangements/ClassificationSchemes.rdf version of this
      ontology was revised to eliminate duplication of concepts in LCC and change the parent class of Classifier to Aspect
      in Analytics.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200701/Arrangements/ClassificationSchemes.rdf version of this
      ontology was revised to eliminate circular definitions.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210201/Arrangements/ClassificationSchemes.rdf version of this
      ontology was revised to address hygiene issues with respect to text formatting and loosen the constraint on classifier
      from classifies something to min 0.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/Arrangements/ClassificationSchemes.rdf version of the
      ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Arrangements/ClassificationSchemes.rdf version of this
      ontology was modified to move the property, 'is conferred on' to the Legal Capacity ontology and to use the Commons
      Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO
      as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/Arrangements/ClassificationSchemes.rdf version of the
      ontology was modified to eliminate deprecations that are more than 6 months old.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2014-2023 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2014-2023 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/20231101/Arrangements/ClassificationSchemes/
  - concept: /concepts/fibo/FND/Arrangements/Arrangements.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Arrangements/
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
    resource: https://www.omg.org/spec/Commons/Designators/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/ClassificationSchemes/
sources:
- id: fibo-source-7338de6177
  resource: references/fibo/FND/Arrangements/ClassificationSchemes.rdf
  sha256: 7338de61776faa661146c3b44c6902fc98da670de604e69439fae05577135627
  title: FIBO source FND/Arrangements/ClassificationSchemes.rdf
title: Classification Schemes Ontology
type: Ontology Definition
---

# Classification Schemes Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/ClassificationSchemes/>

## Relationships

- **Related to**: [Arrangements](/concepts/fibo/FND/Arrangements/Arrangements.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Classifiers](<https://www.omg.org/spec/Commons/Classifiers/>)
- **Related to**: [Designators](<https://www.omg.org/spec/Commons/Designators/>)
- **Related to**: [ClassificationSchemes](<https://spec.edmcouncil.org/fibo/ontology/FND/20231101/Arrangements/ClassificationSchemes/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines abstract concepts for representation of industry classification schemes.
- **license**: https://opensource.org/licenses/MIT
- **label**: Classification Schemes Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20150501/Arrangements/ClassificationSchemes.rdf version of this ontology was introduced as a part of the initial FIBO FBC RFC and revised due to changes introduced in the FIBO 2.0 RFC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Arrangements/ClassificationSchemes.rdf version of this ontology was revised to replace hasDefinition with isDefinedIn to clarify intent.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190701/Arrangements/ClassificationSchemes.rdf version of this ontology was revised to eliminate duplication of concepts in LCC and change the parent class of Classifier to Aspect in Analytics.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200701/Arrangements/ClassificationSchemes.rdf version of this ontology was revised to eliminate circular definitions.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210201/Arrangements/ClassificationSchemes.rdf version of this ontology was revised to address hygiene issues with respect to text formatting and loosen the constraint on classifier from classifies something to min 0.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/Arrangements/ClassificationSchemes.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Arrangements/ClassificationSchemes.rdf version of this ontology was modified to move the property, 'is conferred on' to the Legal Capacity ontology and to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/Arrangements/ClassificationSchemes.rdf version of the ontology was modified to eliminate deprecations that are more than 6 months old.
- **copyright**: Copyright (c) 2014-2023 EDM Council, Inc.
- **copyright**: Copyright (c) 2014-2023 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
