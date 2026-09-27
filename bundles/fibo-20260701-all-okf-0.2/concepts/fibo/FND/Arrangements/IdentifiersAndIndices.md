---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines abstract concepts for representation of indices and indexing schemes, as well as reusable
      identifiers, for reuse in other ontologies.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://purl.org/dc/terms/license
    value: https://opensource.org/licenses/MIT
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Identifiers and Indices Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20140801/Arrangements/IdentifiersAndIndices.rdf version of this
      ontology was introduced as a part of the issue resolutions identified in the FIBO FND 1.0 FTF report and in https://spec.edmcouncil.org/fibo/ontology/FND/1.0/AboutFND-1.0/.
      It was further revised in the FTF in advance of the Long Beach meeting to promote Collection to the top level in the
      hierarchy, resulting in https://spec.edmcouncil.org/fibo/ontology/FND/20141101/Arrangements/Arrangements/.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20141101/Arrangements/IdentifiersAndIndices.rdf version of this
      ontology was revised for the FIBO 2.0 RFC to incorporate mappings to LCC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Arrangements/IdentifiersAndIndices.rdf version of this
      ontology was revised to replace hasDefinition with isDefinedIn to clarify intent.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190701/Arrangements/IdentifiersAndIndices.rdf version of this
      ontology was revised to eliminate duplication of concepts with LCC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200201/Arrangements/IdentifiersAndIndices.rdf version of this
      ontology was revised to add the concept of a time-constrained, reassignable identifier as well as the concept of a composite
      identifier.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20211101/Arrangements/IdentifiersAndIndices.rdf version of this
      ontology was revised loosen a constraint on composite identifier and add regular expression annotations to support ordered
      constituents.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220401/Arrangements/IdentifiersAndIndices.rdf version of the
      ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Arrangements/IdentifiersAndIndices.rdf version of this
      ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes
      (LCC), eliminating redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/Arrangements/IdentifiersAndIndices.rdf version of the
      ontology was modified to eliminate deprecations that are more than 6 months old and to replace content that is now available
      in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20231201/Arrangements/IdentifiersAndIndices.rdf version of the
      ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons)
      v1.1 (FND-380).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2014-2024 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2014-2024 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/20240101/Arrangements/IdentifiersAndIndices/
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
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/ContextualIdentifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Designators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Documents/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Identifiers/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/IdentifiersAndIndices/
sources:
- id: fibo-source-2943e244c9
  resource: references/fibo/FND/Arrangements/IdentifiersAndIndices.rdf
  sha256: 2943e244c9f1e05582f4cd0ce73c69f5f8a148d740aa66d458c621a1ad24f51c
  title: FIBO source FND/Arrangements/IdentifiersAndIndices.rdf
title: Identifiers and Indices Ontology
type: Ontology Definition
---

# Identifiers and Indices Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/IdentifiersAndIndices/>

## Relationships

- **Related to**: [Arrangements](/concepts/fibo/FND/Arrangements/Arrangements.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [CodesAndCodeSets](<https://www.omg.org/spec/Commons/CodesAndCodeSets/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [ContextualIdentifiers](<https://www.omg.org/spec/Commons/ContextualIdentifiers/>)
- **Related to**: [DatesAndTimes](<https://www.omg.org/spec/Commons/DatesAndTimes/>)
- **Related to**: [Designators](<https://www.omg.org/spec/Commons/Designators/>)
- **Related to**: [Documents](<https://www.omg.org/spec/Commons/Documents/>)
- **Related to**: [Identifiers](<https://www.omg.org/spec/Commons/Identifiers/>)
- **Related to**: [IdentifiersAndIndices](<https://spec.edmcouncil.org/fibo/ontology/FND/20240101/Arrangements/IdentifiersAndIndices/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines abstract concepts for representation of indices and indexing schemes, as well as reusable identifiers, for reuse in other ontologies.
- **license**: https://opensource.org/licenses/MIT
- **label**: Identifiers and Indices Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20140801/Arrangements/IdentifiersAndIndices.rdf version of this ontology was introduced as a part of the issue resolutions identified in the FIBO FND 1.0 FTF report and in https://spec.edmcouncil.org/fibo/ontology/FND/1.0/AboutFND-1.0/. It was further revised in the FTF in advance of the Long Beach meeting to promote Collection to the top level in the hierarchy, resulting in https://spec.edmcouncil.org/fibo/ontology/FND/20141101/Arrangements/Arrangements/.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20141101/Arrangements/IdentifiersAndIndices.rdf version of this ontology was revised for the FIBO 2.0 RFC to incorporate mappings to LCC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Arrangements/IdentifiersAndIndices.rdf version of this ontology was revised to replace hasDefinition with isDefinedIn to clarify intent.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190701/Arrangements/IdentifiersAndIndices.rdf version of this ontology was revised to eliminate duplication of concepts with LCC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200201/Arrangements/IdentifiersAndIndices.rdf version of this ontology was revised to add the concept of a time-constrained, reassignable identifier as well as the concept of a composite identifier.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20211101/Arrangements/IdentifiersAndIndices.rdf version of this ontology was revised loosen a constraint on composite identifier and add regular expression annotations to support ordered constituents.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220401/Arrangements/IdentifiersAndIndices.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Arrangements/IdentifiersAndIndices.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/Arrangements/IdentifiersAndIndices.rdf version of the ontology was modified to eliminate deprecations that are more than 6 months old and to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20231201/Arrangements/IdentifiersAndIndices.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **copyright**: Copyright (c) 2014-2024 EDM Council, Inc.
- **copyright**: Copyright (c) 2014-2024 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
