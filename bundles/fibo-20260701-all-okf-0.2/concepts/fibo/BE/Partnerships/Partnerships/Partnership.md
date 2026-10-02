---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: partnership
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: association of two or more legal persons to carry on as co-owners a business for profit
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Partnerships exist in many countries world-wide. Examples of the laws related to the establishment and operation
      of partnerships include the Partnership Act of 1890 in the United Kingdom and the Uniform Partnership Act in the United
      States.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Whether or not partnerships are established through, for example, incorporation, depends on the jurisdiction. Partnerships
      typically not corporations in the US, but can be in Australia and Ghana. See https://legalvision.com.au/what-are-incorporated-limited-partnerships/
      and http://swiftlaw.co/incorporated-partnership/ for additional details.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/ProfitObjective
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasObjective
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
    value: N49e1310b74614bdc851033b887fe065d
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/PartnershipAgreement
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy
  subclass_of:
  - concept: /concepts/fibo/BE/LegalEntities/LegalPersons/BusinessEntity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/BusinessEntity
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/LegalEntity
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/Partnership
sources:
- id: fibo-source-d8e7bd00bc
  resource: references/fibo/BE/Partnerships/Partnerships.rdf
  sha256: d8e7bd00bcec02116a8ba944082e7c83bd17338e42c9b9925e2ef483b7e1cacf
  title: FIBO source BE/Partnerships/Partnerships.rdf
title: partnership
type: Ontology Class
---

# partnership

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/Partnership>

## Definition

association of two or more legal persons to carry on as co-owners a business for profit

## Relationships

- **Subclass of**: [BusinessEntity](/concepts/fibo/BE/LegalEntities/LegalPersons/BusinessEntity.md)
- **Subclass of**: [LegalEntity](<https://www.omg.org/spec/Commons/Organizations/LegalEntity>)

## Constraints

- **[hasObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasObjective.md)**: min qualified cardinality 0 of type [ProfitObjective](/concepts/fibo/BE/LegalEntities/LegalPersons/ProfitObjective.md)
- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from value `N49e1310b74614bdc851033b887fe065d`
- **[isGovernedBy](<https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy>)**: some values from of type [PartnershipAgreement](/concepts/fibo/BE/Partnerships/Partnerships/PartnershipAgreement.md)

## Annotations

- **label**: partnership
- **definition**: association of two or more legal persons to carry on as co-owners a business for profit
- **explanatoryNote**: Partnerships exist in many countries world-wide. Examples of the laws related to the establishment and operation of partnerships include the Partnership Act of 1890 in the United Kingdom and the Uniform Partnership Act in the United States.
- **explanatoryNote**: Whether or not partnerships are established through, for example, incorporation, depends on the jurisdiction. Partnerships typically not corporations in the US, but can be in Australia and Ghana. See https://legalvision.com.au/what-are-incorporated-limited-partnerships/ and http://swiftlaw.co/incorporated-partnership/ for additional details.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
