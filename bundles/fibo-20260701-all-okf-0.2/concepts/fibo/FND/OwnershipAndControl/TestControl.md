---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines a set of test parties and control situations to test their underlying control relations.
  - predicate: http://purl.org/dc/terms/contributor
    value: Adaptive, Inc.
  - predicate: http://purl.org/dc/terms/contributor
    value: Thematix Partners LLC
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://purl.org/dc/terms/license
    value: https://opensource.org/licenses/MIT
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Financial Industry Business Ontology (FIBO) Test Control Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210401/OwnershipAndControl/TestControl.rdf version of the ontology
      was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: "This version of the ontology was revised in advance of the September 2013 New Brunswick, NJ meeting, as follows:\n\
      \   (1) to use slash style URI/IRIss (also called 303 URIs, vs. hash style) as required to support server side processing\
      \ \n   (2) to use version-independent IRIs for all definitions internally as opposed to version-specific IRIs\n   (3)\
      \ to change the file suffix from .owl to .rdf to increase usability in RDF tools\n   (4) to use 4-level abbreviations\
      \ and corresponding namespace prefixes for all FIBO ontologies, reflecting a family/specification/module/ontology structure\n\
      \   (5) to incorporate changes to the specification metadata to support documentation at the family, specification,\
      \ module, and ontology level, similar to the abbreviations\n   (6) to move the ontology from the Utilities module to\
      \ an independent TemporalRelations module\n   (7) to revise a number of definitions, per discussion with various stakeholders.\n\
      \   (8) to augment the definitions to include entity names from Business Entities."
  - predicate: http://www.w3.org/2004/02/skos/core#historyNote
    value: "This version of the FIBO Foundations Specification was revised primarily to reflect comments received at the March\
      \ 2013 OMG Technical Meeting in Reston and reflected in the Errata discussed at the June 2013 OMG Technical Meeting\
      \ in Berlin. \n\nRevisions to FIBO Foundations are managed per the process outlined in the Policies and Procedures for\
      \ OMG standards, with the intent to maintain backwards compatibility in the ontologies to the degree possible.\n  \n\
      The RDF/XML serialized OWL for the Foundations ODM/OWL ontologies have been checked for syntactic errors and logical\
      \ consistency with Protege 4 (http://protege.stanford.edu/), HermiT 1.3.7 (http://www.hermit-reasoner.com/) and Pellet\
      \ 2.2 (http://clarkparsia.com/pellet/)."
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2024 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2024 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/20240101/OwnershipAndControl/TestControl/
  - concept: /concepts/fibo/FND/Organizations/TestFormalOrganizations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/TestFormalOrganizations/
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Informative.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Informative
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/TestControl/
sources:
- id: fibo-source-267ef337b0
  resource: references/fibo/etc/testing/data/fnd/OwnershipAndControl/TestControl.rdf
  sha256: 267ef337b05b30bec2b788b9cf8cd19e1c4d21c4862199a4afe6f6fb1a9a52e5
  title: FIBO source etc/testing/data/fnd/OwnershipAndControl/TestControl.rdf
title: Financial Industry Business Ontology (FIBO) Test Control Ontology
type: Ontology Definition
---

# Financial Industry Business Ontology (FIBO) Test Control Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/TestControl/>

## Relationships

- **Related to**: [TestFormalOrganizations](/concepts/fibo/FND/Organizations/TestFormalOrganizations.md)
- **Related to**: [Control](/concepts/fibo/FND/OwnershipAndControl/Control.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [PartiesAndSituations](<https://www.omg.org/spec/Commons/PartiesAndSituations/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [TestControl](<https://spec.edmcouncil.org/fibo/ontology/FND/20240101/OwnershipAndControl/TestControl/>)
- **Related to**: [Informative](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Informative.md)

## Annotations

- **abstract**: This ontology defines a set of test parties and control situations to test their underlying control relations.
- **contributor**: Adaptive, Inc.
- **contributor**: Thematix Partners LLC
- **license**: https://opensource.org/licenses/MIT
- **label**: Financial Industry Business Ontology (FIBO) Test Control Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210401/OwnershipAndControl/TestControl.rdf version of the ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: This version of the ontology was revised in advance of the September 2013 New Brunswick, NJ meeting, as follows:    (1) to use slash style URI/IRIss (also called 303 URIs, vs. hash style) as required to support server side processing     (2) to use version-independent IRIs for all definitions internally as opposed to version-specific IRIs    (3) to change the file suffix from .owl to .rdf to increase usability in RDF tools    (4) to use 4-level abbreviations and corresponding namespace prefixes for all FIBO ontologies, reflecting a family/specification/module/ontology structure    (5) to incorporate changes to the specification metadata to support documentation at the family, specification, module, and ontology level, similar to the abbreviations    (6) to move the ontology from the Utilities module to an independent TemporalRelations module    (7) to revise a number of definitions, per discussion with various stakeholders.    (8) to augment the definitions to include entity names from Business Entities.
- **historyNote**: This version of the FIBO Foundations Specification was revised primarily to reflect comments received at the March 2013 OMG Technical Meeting in Reston and reflected in the Errata discussed at the June 2013 OMG Technical Meeting in Berlin.   Revisions to FIBO Foundations are managed per the process outlined in the Policies and Procedures for OMG standards, with the intent to maintain backwards compatibility in the ontologies to the degree possible.    The RDF/XML serialized OWL for the Foundations ODM/OWL ontologies have been checked for syntactic errors and logical consistency with Protege 4 (http://protege.stanford.edu/), HermiT 1.3.7 (http://www.hermit-reasoner.com/) and Pellet 2.2 (http://clarkparsia.com/pellet/).
- **copyright**: Copyright (c) 2013-2024 EDM Council, Inc.
- **copyright**: Copyright (c) 2013-2024 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
