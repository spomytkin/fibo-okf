---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology brings the concepts of ownership and control together, in cases where the combined semantics are
      applicable, such as for a wholly owned subsidiary.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://purl.org/dc/terms/license
    value: https://opensource.org/licenses/MIT
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Ownership and Control Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/OwnershipAndControl/OwnershipAndControl.rdf version
      of the ontology was modified to better integrate it with the situation pattern and eliminate circular definitions.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210201/OwnershipAndControl/OwnershipAndControl.rdf version
      of the ontology was modified to integrate the properties defined herein with the ownership and control patterns.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20211201/OwnershipAndControl/OwnershipAndControl.rdf version
      of the ontology was modified to address hygiene issues with respect to text formatting.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/OwnershipAndControl/OwnershipAndControl.rdf version
      of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's
      Specification Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/OwnershipAndControl/OwnershipAndControl.rdf version
      of the ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons)
      v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: This ontology was added to Foundations in advance of the December 2014 Long Beach meeting in support of the issue
      resolutions identified in the FIBO FND 1.0 FTF report and in https://spec.edmcouncil.org/fibo/ontology/FND/1.0/AboutFND-1.0/.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2024 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2024 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/20240101/OwnershipAndControl/OwnershipAndControl/
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/
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
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/OwnershipAndControl/
sources:
- id: fibo-source-e6e2018aa7
  resource: references/fibo/FND/OwnershipAndControl/OwnershipAndControl.rdf
  sha256: e6e2018aa7f8cb7c2fab2505906a5311b9e6a797e599133ddfb4fac1365a432f
  title: FIBO source FND/OwnershipAndControl/OwnershipAndControl.rdf
title: Ownership and Control Ontology
type: Ontology Definition
---

# Ownership and Control Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/OwnershipAndControl/>

## Relationships

- **Related to**: [Control](/concepts/fibo/FND/OwnershipAndControl/Control.md)
- **Related to**: [Ownership](/concepts/fibo/FND/OwnershipAndControl/Ownership.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [PartiesAndSituations](<https://www.omg.org/spec/Commons/PartiesAndSituations/>)
- **Related to**: [OwnershipAndControl](<https://spec.edmcouncil.org/fibo/ontology/FND/20240101/OwnershipAndControl/OwnershipAndControl/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology brings the concepts of ownership and control together, in cases where the combined semantics are applicable, such as for a wholly owned subsidiary.
- **license**: https://opensource.org/licenses/MIT
- **label**: Ownership and Control Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/OwnershipAndControl/OwnershipAndControl.rdf version of the ontology was modified to better integrate it with the situation pattern and eliminate circular definitions.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210201/OwnershipAndControl/OwnershipAndControl.rdf version of the ontology was modified to integrate the properties defined herein with the ownership and control patterns.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20211201/OwnershipAndControl/OwnershipAndControl.rdf version of the ontology was modified to address hygiene issues with respect to text formatting.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/OwnershipAndControl/OwnershipAndControl.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/OwnershipAndControl/OwnershipAndControl.rdf version of the ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: This ontology was added to Foundations in advance of the December 2014 Long Beach meeting in support of the issue resolutions identified in the FIBO FND 1.0 FTF report and in https://spec.edmcouncil.org/fibo/ontology/FND/1.0/AboutFND-1.0/.
- **copyright**: Copyright (c) 2013-2024 EDM Council, Inc.
- **copyright**: Copyright (c) 2013-2024 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
