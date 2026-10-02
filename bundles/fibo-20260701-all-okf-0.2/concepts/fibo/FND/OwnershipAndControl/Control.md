---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines high-level, control-related concepts, including the distinction between de jure and de facto
      control, the former being derived with reference to terms in the Legal Capacity ontology.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://purl.org/dc/terms/license
    value: https://opensource.org/licenses/MIT
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Control Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: "The http://www.omg.org/spec/FIBO/Foundations/20130601/OwnershipAndControl/Control.owl version of the ontology\
      \ was revised in advance of the September 2013 New Brunswick, NJ meeting, as follows:\n\t(1) to use slash style URI/IRIss\
      \ (also called 303 URIs, vs. hash style) as required to support server side processing \n\t(2) to use version-independent\
      \ IRIs for all definitions internally as opposed to version-specific IRIs\n\t(3) to change the file suffix from .owl\
      \ to .rdf to increase usability in RDF tools\n\t(4) to use 4-level abbreviations and corresponding namespace prefixes\
      \ for all FIBO ontologies, reflecting a family/specification/module/ontology structure\n\t(5) to incorporate changes\
      \ to the specification metadata to support documentation at the family, specification, module, and ontology level, similar\
      \ to the abbreviations."
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20130801/OwnershipAndControl/Control.rdf version of the ontology
      was was modified per the issue resolutions identified in the FIBO FND 1.0 FTF report and in https://spec.edmcouncil.org/fibo/ontology/FND/1.0/AboutFND-1.0/.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/OwnershipAndControl/Control.rdf version of the ontology
      was modified to integrate the concept of a situation, situational roles, and corresponding relations with the definition
      of control and eliminate minimum cardinality of 1 restrictions.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200601/OwnershipAndControl/Control.rdf version of the ontology
      was modified to simplify control concepts and relations, complete the control patterns, and eliminate ambiguity in definitions.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20201201/OwnershipAndControl/Control.rdf version of the ontology
      was modified to eliminate references to external dictionary sites that no longer resolve.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210101/OwnershipAndControl/Control.rdf version of the ontology
      was modified to incorporate the latest insights into how control relations should integrate with the control situation
      and to unwind confusion around the various properties used to represent aspects of control with respect to their domains
      and ranges.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210401/OwnershipAndControl/Control.rdf version of the ontology
      was modified to address hygiene issues with respect to text formatting.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/OwnershipAndControl/Control.rdf version of the ontology
      was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/OwnershipAndControl/Control.rdf version of this ontology
      was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC),
      eliminating redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/OwnershipAndControl/Control.rdf version of this ontology
      was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2024 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2024 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/20240101/OwnershipAndControl/Control/
  - concept: /concepts/fibo/FND/Law/LegalCapacity.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/
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
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/
sources:
- id: fibo-source-b62f5055c5
  resource: references/fibo/FND/OwnershipAndControl/Control.rdf
  sha256: b62f5055c539290530c387d27526ed613d4570b7c04105acfa6a5bc91f8e7569
  title: FIBO source FND/OwnershipAndControl/Control.rdf
title: Control Ontology
type: Ontology Definition
---

# Control Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/>

## Relationships

- **Related to**: [LegalCapacity](/concepts/fibo/FND/Law/LegalCapacity.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [DatesAndTimes](<https://www.omg.org/spec/Commons/DatesAndTimes/>)
- **Related to**: [PartiesAndSituations](<https://www.omg.org/spec/Commons/PartiesAndSituations/>)
- **Related to**: [Control](<https://spec.edmcouncil.org/fibo/ontology/FND/20240101/OwnershipAndControl/Control/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines high-level, control-related concepts, including the distinction between de jure and de facto control, the former being derived with reference to terms in the Legal Capacity ontology.
- **license**: https://opensource.org/licenses/MIT
- **label**: Control Ontology
- **changeNote**: The http://www.omg.org/spec/FIBO/Foundations/20130601/OwnershipAndControl/Control.owl version of the ontology was revised in advance of the September 2013 New Brunswick, NJ meeting, as follows: 	(1) to use slash style URI/IRIss (also called 303 URIs, vs. hash style) as required to support server side processing  	(2) to use version-independent IRIs for all definitions internally as opposed to version-specific IRIs 	(3) to change the file suffix from .owl to .rdf to increase usability in RDF tools 	(4) to use 4-level abbreviations and corresponding namespace prefixes for all FIBO ontologies, reflecting a family/specification/module/ontology structure 	(5) to incorporate changes to the specification metadata to support documentation at the family, specification, module, and ontology level, similar to the abbreviations.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20130801/OwnershipAndControl/Control.rdf version of the ontology was was modified per the issue resolutions identified in the FIBO FND 1.0 FTF report and in https://spec.edmcouncil.org/fibo/ontology/FND/1.0/AboutFND-1.0/.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/OwnershipAndControl/Control.rdf version of the ontology was modified to integrate the concept of a situation, situational roles, and corresponding relations with the definition of control and eliminate minimum cardinality of 1 restrictions.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200601/OwnershipAndControl/Control.rdf version of the ontology was modified to simplify control concepts and relations, complete the control patterns, and eliminate ambiguity in definitions.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20201201/OwnershipAndControl/Control.rdf version of the ontology was modified to eliminate references to external dictionary sites that no longer resolve.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210101/OwnershipAndControl/Control.rdf version of the ontology was modified to incorporate the latest insights into how control relations should integrate with the control situation and to unwind confusion around the various properties used to represent aspects of control with respect to their domains and ranges.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210401/OwnershipAndControl/Control.rdf version of the ontology was modified to address hygiene issues with respect to text formatting.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/OwnershipAndControl/Control.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/OwnershipAndControl/Control.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/OwnershipAndControl/Control.rdf version of this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **copyright**: Copyright (c) 2013-2024 EDM Council, Inc.
- **copyright**: Copyright (c) 2013-2024 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
