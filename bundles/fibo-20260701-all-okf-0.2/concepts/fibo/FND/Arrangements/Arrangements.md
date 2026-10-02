---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines abstract structural concepts, extending the Commons concept of an arrangement to represent
      schemes.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://purl.org/dc/terms/license
    value: https://opensource.org/licenses/MIT
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Arrangements Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20140801/Arrangements/Arrangements.rdf version of this ontology
      was introduced as a part of the issue resolutions identified in the FIBO FND 1.0 FTF report and in https://spec.edmcouncil.org/fibo/ontology/FND/1.0/AboutFND-1.0/.
      It was further revised in the FTF in advance of the Long Beach meeting to promote Collection to the top level in the
      hierarchy, resulting in https://spec.edmcouncil.org/fibo/ontology/FND/20141101/Arrangements/Arrangements/.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20141101/Arrangements/Arrangements.rdf version of this ontology
      was revised as a part of the issue resolutions identified in the FIBO FND 1.2 RTF report to add a definition for a structured
      collection.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20170201/Arrangements/Arrangements.rdf version of this ontology
      was revised for the FIBO 2.0 RFC report to add a general definition for scheme, add dated collection, and add mappings
      to LCC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Arrangements/Arrangements.rdf version of this ontology
      was revised to loosen the range on hasObservedDateTime such that it can be used more generally.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190201/Arrangements/Arrangements.rdf version of this ontology
      was revised to loosen the restriction on hasObservedDateTime so that it can be used with the new CombinedDateTime datatype
      (in FinancialDates, which is not imported herein to avoid circular dependencies), with finer granularity than seconds
      as appropriate for trades, for example.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190401/Arrangements/Arrangements.rdf version of this ontology
      was revised to eliminate duplication with concepts in LCC for classes including arrangement, collection, code element,
      code set, etc to simplify the hierarchy and usage for FIBO users.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200201/Arrangements/Arrangements.rdf version of this ontology
      was revised to move the concepts of a dated collection and dated collection constituent to Financial Dates in order
      to improve usability and simplify reasoning and make definitions ISO 704 compliant.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200701/Arrangements/Arrangements.rdf version of this ontology
      was revised to add a restriction to structured collection pointing to the arrangement used to organize that collection,
      and to revise the definition accordingly.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210901/Arrangements/Arrangements.rdf version of this ontology
      was revised to address hygiene issues with respect to text formatting.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/Arrangements/Arrangements.rdf version of the ontology
      was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230201/Arrangements/Arrangements.rdf version of this ontology
      was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC),
      eliminating redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/Arrangements/Arrangements.rdf version of the ontology
      was modified to eliminate deprecations that are more than 6 months old.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2014-2023 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2014-2023 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/20231101/Arrangements/Arrangements/
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
    resource: https://www.omg.org/spec/Commons/Designators/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Arrangements/
sources:
- id: fibo-source-40d4a97d42
  resource: references/fibo/FND/Arrangements/Arrangements.rdf
  sha256: 40d4a97d42efcf7a35be65975208192604f5ce601e40c41ef201dc2032c9eb79
  title: FIBO source FND/Arrangements/Arrangements.rdf
title: Arrangements Ontology
type: Ontology Definition
---

# Arrangements Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Arrangements/>

## Relationships

- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [CodesAndCodeSets](<https://www.omg.org/spec/Commons/CodesAndCodeSets/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [Designators](<https://www.omg.org/spec/Commons/Designators/>)
- **Related to**: [Arrangements](<https://spec.edmcouncil.org/fibo/ontology/FND/20231101/Arrangements/Arrangements/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines abstract structural concepts, extending the Commons concept of an arrangement to represent schemes.
- **license**: https://opensource.org/licenses/MIT
- **label**: Arrangements Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20140801/Arrangements/Arrangements.rdf version of this ontology was introduced as a part of the issue resolutions identified in the FIBO FND 1.0 FTF report and in https://spec.edmcouncil.org/fibo/ontology/FND/1.0/AboutFND-1.0/. It was further revised in the FTF in advance of the Long Beach meeting to promote Collection to the top level in the hierarchy, resulting in https://spec.edmcouncil.org/fibo/ontology/FND/20141101/Arrangements/Arrangements/.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20141101/Arrangements/Arrangements.rdf version of this ontology was revised as a part of the issue resolutions identified in the FIBO FND 1.2 RTF report to add a definition for a structured collection.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20170201/Arrangements/Arrangements.rdf version of this ontology was revised for the FIBO 2.0 RFC report to add a general definition for scheme, add dated collection, and add mappings to LCC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Arrangements/Arrangements.rdf version of this ontology was revised to loosen the range on hasObservedDateTime such that it can be used more generally.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190201/Arrangements/Arrangements.rdf version of this ontology was revised to loosen the restriction on hasObservedDateTime so that it can be used with the new CombinedDateTime datatype (in FinancialDates, which is not imported herein to avoid circular dependencies), with finer granularity than seconds as appropriate for trades, for example.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190401/Arrangements/Arrangements.rdf version of this ontology was revised to eliminate duplication with concepts in LCC for classes including arrangement, collection, code element, code set, etc to simplify the hierarchy and usage for FIBO users.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200201/Arrangements/Arrangements.rdf version of this ontology was revised to move the concepts of a dated collection and dated collection constituent to Financial Dates in order to improve usability and simplify reasoning and make definitions ISO 704 compliant.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200701/Arrangements/Arrangements.rdf version of this ontology was revised to add a restriction to structured collection pointing to the arrangement used to organize that collection, and to revise the definition accordingly.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210901/Arrangements/Arrangements.rdf version of this ontology was revised to address hygiene issues with respect to text formatting.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/Arrangements/Arrangements.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230201/Arrangements/Arrangements.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/Arrangements/Arrangements.rdf version of the ontology was modified to eliminate deprecations that are more than 6 months old.
- **copyright**: Copyright (c) 2014-2023 EDM Council, Inc.
- **copyright**: Copyright (c) 2014-2023 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
