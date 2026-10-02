---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: judiciary
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: branch of government that comprises the system of courts that interprets and applies the law in the name of the
      supranational, national, federal, or regional government, depending on its jurisdiction
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The judiciary also provides a mechanism for the resolution of disputes. Under the doctrine of the separation of
      powers, the judiciary generally does not make law (that is, in a plenary fashion, which is the responsibility of the
      legislature) or enforce law (which is the responsibility of the executive), but rather interprets law and applies it
      to the facts of each case.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/CourtOfLaw
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasPart
  subclass_of:
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities/BranchOfGovernment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/BranchOfGovernment
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Judiciary
sources:
- id: fibo-source-5deab1a754
  resource: references/fibo/BE/GovernmentEntities/GovernmentEntities.rdf
  sha256: 5deab1a75487a8f7ff902b567d86099df6c1e24acc1a3a06d0351785ed1d30d3
  title: FIBO source BE/GovernmentEntities/GovernmentEntities.rdf
title: judiciary
type: Ontology Class
---

# judiciary

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Judiciary>

## Definition

branch of government that comprises the system of courts that interprets and applies the law in the name of the supranational, national, federal, or regional government, depending on its jurisdiction

## Relationships

- **Subclass of**: [BranchOfGovernment](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/BranchOfGovernment.md)

## Constraints

- **[hasPart](<https://www.omg.org/spec/Commons/Collections/hasPart>)**: some values from of type [CourtOfLaw](/concepts/fibo/FND/Law/LegalCore/CourtOfLaw.md)

## Annotations

- **label**: judiciary
- **definition**: branch of government that comprises the system of courts that interprets and applies the law in the name of the supranational, national, federal, or regional government, depending on its jurisdiction
- **explanatoryNote**: The judiciary also provides a mechanism for the resolution of disputes. Under the doctrine of the separation of powers, the judiciary generally does not make law (that is, in a plenary fashion, which is the responsibility of the legislature) or enforce law (which is the responsibility of the executive), but rather interprets law and applies it to the facts of each case.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
