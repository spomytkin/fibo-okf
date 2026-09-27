---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: government minister
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: government official that is an executive, who is either appointed or elected to a high office in the government
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Minister of Finance, Secretary of State, Attorney General of California
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities/GovernmentOfficial.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentOfficial
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives/Executive.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/Executive
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentMinister
sources:
- id: fibo-source-5deab1a754
  resource: references/fibo/BE/GovernmentEntities/GovernmentEntities.rdf
  sha256: 5deab1a75487a8f7ff902b567d86099df6c1e24acc1a3a06d0351785ed1d30d3
  title: FIBO source BE/GovernmentEntities/GovernmentEntities.rdf
title: government minister
type: Ontology Class
---

# government minister

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentMinister>

## Definition

government official that is an executive, who is either appointed or elected to a high office in the government

## Relationships

- **Subclass of**: [GovernmentOfficial](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/GovernmentOfficial.md)
- **Subclass of**: [Executive](/concepts/fibo/BE/OwnershipAndControl/Executives/Executive.md)

## Annotations

- **label**: government minister
- **definition**: government official that is an executive, who is either appointed or elected to a high office in the government
- **example**: Minister of Finance, Secretary of State, Attorney General of California

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
