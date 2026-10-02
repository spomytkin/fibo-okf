---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: non-governmental organization
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: not-for-profit organization that functions independently of government
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: NGO
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: NGOs, sometimes called civil societies, are organized on community, national and international levels to serve
      specific social or political purposes, and are cooperative, rather than commercial, in nature.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Some NGOs avoid formal funding altogether and are run primarily by volunteers. NGOs are highly diverse groups of
      organizations engaged in a wide range of activities, and take different forms in different parts of the world. Some
      may have charitable status, while others may be registered for tax exemption based on recognition of social purposes.
      Others may be fronts for political, religious, or other interests.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/PublicPurpose
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasObjective
  subclass_of:
  - concept: /concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations/NotForProfitOrganization.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/NotForProfitOrganization
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/NonGovernmentalOrganization
sources:
- id: fibo-source-9758af6c79
  resource: references/fibo/BE/LegalEntities/FormalBusinessOrganizations.rdf
  sha256: 9758af6c796f157eedb21d72cde0822cb7a2ecbd6b5a70ef23be48121c598ede
  title: FIBO source BE/LegalEntities/FormalBusinessOrganizations.rdf
title: non-governmental organization
type: Ontology Class
---

# non-governmental organization

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/NonGovernmentalOrganization>

## Definition

not-for-profit organization that functions independently of government

## Relationships

- **Subclass of**: [NotForProfitOrganization](/concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations/NotForProfitOrganization.md)

## Constraints

- **[hasObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasObjective.md)**: min qualified cardinality 0 of type [PublicPurpose](/concepts/fibo/BE/LegalEntities/LegalPersons/PublicPurpose.md)

## Annotations

- **label**: non-governmental organization
- **definition**: not-for-profit organization that functions independently of government
- **abbreviation**: NGO
- **explanatoryNote**: NGOs, sometimes called civil societies, are organized on community, national and international levels to serve specific social or political purposes, and are cooperative, rather than commercial, in nature.
- **explanatoryNote**: Some NGOs avoid formal funding altogether and are run primarily by volunteers. NGOs are highly diverse groups of organizations engaged in a wide range of activities, and take different forms in different parts of the world. Some may have charitable status, while others may be registered for tax exemption based on recognition of social purposes. Others may be fronts for political, religious, or other interests.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
