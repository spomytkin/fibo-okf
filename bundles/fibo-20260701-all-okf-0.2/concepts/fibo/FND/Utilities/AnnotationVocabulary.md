---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: "This vocabulary provides a set of metadata annotations for use in describing FIBO ontology elements. The annotations\
      \ extend properties defined in the OMG's Commons Ontology Library (Commons) Annotation Vocabulary, in the Dublin Core\
      \ Metadata Terms Vocabulary and in the W3C Simple Knowledge Organization System (SKOS) Vocabulary, and have been customized\
      \ to suit the FIBO specification development process. \n\nNote that any of the original properties provided in Dublin\
      \ Core and SKOS can be used in addition to the terms provided herein. However, any Dublin Core terms that are not explicitly\
      \ defined as OWL annotation properties in this ontology or in any of its imports must be so declared in the ontologies\
      \ that use them."
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://purl.org/dc/terms/license
    value: https://opensource.org/licenses/MIT
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: FIBO Annotation Vocabulary
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The http://www.omg.org/spec/EDMC-FIBO/FND/20130801/Utilities/AnnotationVocabulary.rdf version of this ontology
      was modified per the issue resolutions identified in the FIBO FND 1.0 FTF report and in http://www.omg.org/spec/EDMC-FIBO/FND/1.0/AboutFND-1.0/.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: "The http://www.omg.org/spec/FIBO/Foundations/20130601/Utilities/AnnotationVocabulary.owl version of the ontology\
      \ was revised in advance of the September 2013 New Brunswick, NJ meeting, as follows:\n\t(1) to use slash style URI/IRIss\
      \ (also called 303 URIs, vs. hash style) as required to support server side processing \n\t(2) to use version-independent\
      \ IRIs for all definitions internally as opposed to version-specific IRIs\n\t(3) to change the file suffix from .owl\
      \ to .rdf to increase usability in RDF tools\n\t(4) to use 4-level abbreviations and corresponding namespace prefixes\
      \ for all FIBO ontologies, reflecting a family/specification/module/ontology structure\n\t(5) to incorporate changes\
      \ to the specification metadata to support documentation at the family, specification, module, and ontology level, similar\
      \ to the abbreviations"
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Utilities/AnnotationVocabulary.rdf version of this ontology
      was modified to add the symbol annotation.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190501/Utilities/AnnotationVocabulary.rdf version of this ontology
      was modified to eliminate deprecated properties.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190901/Utilities/AnnotationVocabulary.rdf version of this ontology
      was modified to add common and preferred designations as needed for postal addresses and other purposes, to correct
      named individuals to be properly declared, and to revise definitions to be ISO 704 compliant.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200301/Utilities/AnnotationVocabulary.rdf version of this ontology
      was modified to eliminate skos:Concept as a superclass of MaturityLevel (replaced with LifecycleStage in the Lifecycles
      ontology), revise explanatory notes for maturity levels based on community feedback, and correct the subproperty inheritance
      for adaptedFrom and logicalDefinition.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200601/Utilities/AnnotationVocabulary.rdf version of this ontology
      was modified to address hygiene issues with respect to text formatting and eliminate the explicit SKOS import which
      is not needed.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/Utilities/AnnotationVocabulary.rdf version of this ontology
      was modified to integrate the Commons Ontology Library (Commons) Annotation Vocabulary and eliminate the need to import
      the OMG's Specification Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Utilities/AnnotationVocabulary.rdf version of the ontology
      was modified to eliminate deprecations that are more than 6 months old.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2023 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2023 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/20231101/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Classifiers/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
sources:
- id: fibo-source-b35d351e6d
  resource: references/fibo/FND/Utilities/AnnotationVocabulary.rdf
  sha256: b35d351e6d0d981175c56d3b40476b13e64e7b6ed90dd4fd030ececd6f23a2dd
  title: FIBO source FND/Utilities/AnnotationVocabulary.rdf
title: FIBO Annotation Vocabulary
type: Ontology Definition
---

# FIBO Annotation Vocabulary

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/>

## Relationships

- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Classifiers](<https://www.omg.org/spec/Commons/Classifiers/>)
- **Related to**: [AnnotationVocabulary](<https://spec.edmcouncil.org/fibo/ontology/FND/20231101/Utilities/AnnotationVocabulary/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This vocabulary provides a set of metadata annotations for use in describing FIBO ontology elements. The annotations extend properties defined in the OMG's Commons Ontology Library (Commons) Annotation Vocabulary, in the Dublin Core Metadata Terms Vocabulary and in the W3C Simple Knowledge Organization System (SKOS) Vocabulary, and have been customized to suit the FIBO specification development process.   Note that any of the original properties provided in Dublin Core and SKOS can be used in addition to the terms provided herein. However, any Dublin Core terms that are not explicitly defined as OWL annotation properties in this ontology or in any of its imports must be so declared in the ontologies that use them.
- **license**: https://opensource.org/licenses/MIT
- **label**: FIBO Annotation Vocabulary
- **changeNote**: The http://www.omg.org/spec/EDMC-FIBO/FND/20130801/Utilities/AnnotationVocabulary.rdf version of this ontology was modified per the issue resolutions identified in the FIBO FND 1.0 FTF report and in http://www.omg.org/spec/EDMC-FIBO/FND/1.0/AboutFND-1.0/.
- **changeNote**: The http://www.omg.org/spec/FIBO/Foundations/20130601/Utilities/AnnotationVocabulary.owl version of the ontology was revised in advance of the September 2013 New Brunswick, NJ meeting, as follows: 	(1) to use slash style URI/IRIss (also called 303 URIs, vs. hash style) as required to support server side processing  	(2) to use version-independent IRIs for all definitions internally as opposed to version-specific IRIs 	(3) to change the file suffix from .owl to .rdf to increase usability in RDF tools 	(4) to use 4-level abbreviations and corresponding namespace prefixes for all FIBO ontologies, reflecting a family/specification/module/ontology structure 	(5) to incorporate changes to the specification metadata to support documentation at the family, specification, module, and ontology level, similar to the abbreviations
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Utilities/AnnotationVocabulary.rdf version of this ontology was modified to add the symbol annotation.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190501/Utilities/AnnotationVocabulary.rdf version of this ontology was modified to eliminate deprecated properties.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190901/Utilities/AnnotationVocabulary.rdf version of this ontology was modified to add common and preferred designations as needed for postal addresses and other purposes, to correct named individuals to be properly declared, and to revise definitions to be ISO 704 compliant.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200301/Utilities/AnnotationVocabulary.rdf version of this ontology was modified to eliminate skos:Concept as a superclass of MaturityLevel (replaced with LifecycleStage in the Lifecycles ontology), revise explanatory notes for maturity levels based on community feedback, and correct the subproperty inheritance for adaptedFrom and logicalDefinition.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200601/Utilities/AnnotationVocabulary.rdf version of this ontology was modified to address hygiene issues with respect to text formatting and eliminate the explicit SKOS import which is not needed.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/Utilities/AnnotationVocabulary.rdf version of this ontology was modified to integrate the Commons Ontology Library (Commons) Annotation Vocabulary and eliminate the need to import the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Utilities/AnnotationVocabulary.rdf version of the ontology was modified to eliminate deprecations that are more than 6 months old.
- **copyright**: Copyright (c) 2013-2023 EDM Council, Inc.
- **copyright**: Copyright (c) 2013-2023 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
